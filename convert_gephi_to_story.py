# Pulling Data from Gephi export to simplify import to Personas
import os
import argparse
import psycopg2
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
django.setup()

from personas.models import StoryObject, Story, Relationship
import csv

nodes = {}
edges = []

def parse_nodes_and_edges(story_name):

    story=Story.objects.get(title="London Fog")

    with open(story_name + '_nodes.csv', 'r') as f:
        data = csv.DictReader(f)

        for d in data:
            node_id = d['Id']
            name = d['name']
            role = d['Label']
            description = d['Background']
            nodes[node_id] = {"name": name, "role": role,
            "description": description}

    with open(story_name + '_edges.csv', 'r') as f:
        next(f)
        data = csv.reader(f)

        for d in data:
            source, target, directed, edge_id, relationship_class, weight = d
            edges.append([source, target, relationship_class])

    for node in nodes:
        try:
            s = StoryObject.objects.get_or_create(
                name=nodes[node]['name'],
                role=nodes[node]['role'],
                description=nodes[node]['description'],
                story=story,
                creator=User.objects.get(username="christopherallison"))

            print("StoryObjects converted: {}".format(nodes[node]['name']))

        except psycopg2.IntegrityError:
            print("StoryObjects {} already exists".format(nodes[node]['name']))
            pass

    for edge in edges:
        source, target, relationship_class = edge
        r = Relationship.objects.get_or_create(
            from_storyobject = StoryObject.objects.get(
            name=nodes[source]['name'], story=story),
            to_storyobject = StoryObject.objects.get(
            name=nodes[target]['name'], story=story),
            relationship_class = relationship_class[:32],
            weight=5, relationship_description="To be added")

        print("Relationship added between {} and {}".format(
            nodes[source]['name'],
            nodes[target]['name']))

    print("Done and successful.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--story", required=True, help="Story title and file previx")
    args = vars(ap.parse_args())

    story_title = args['story']

    parse_nodes_and_edges(story_title)
