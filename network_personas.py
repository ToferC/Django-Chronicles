import json
import networkx as nx
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
import django
django.setup()
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models import F, Q

from personas.models import StoryObject, Statistic, Skill, Ability, Aspect, CombatInfo, Relationship

node_shapes = {}
node_colors = {}

simple_colours = []

def find_colour(story_object):
    if story_object.c_type == "Character":
        node_shapes[story_object.name] = 'o'
        node_colors[story_object.name] = 'r'
    elif story_object.c_type == "Organization":
        node_shapes[story_object.name] = 'h'
        node_colors[story_object.name] = 'b'
    elif story_object.c_type == "Creature":
        node_shapes[story_object.name] = '^'
        node_colors[story_object.name] = 'g'
    elif story_object.c_type == "Force":
        node_shapes[story_object.name] = 'v'
        node_colors[story_object.name] = 'c'
    elif story_object.c_type == "Thing":
        node_shapes[story_object.name] = 's'
        node_colors[story_object.name] = 'y'

def return_json_graph(graph_subject):

    story_objects = {}
    labels = {}

    target = StoryObject.objects.get(name=graph_subject)

    neighbours = Relationship.objects.filter(
                Q(from_storyobject__name=target.name) |
                Q(to_storyobject__name=target.name))

    story_objects[target] = target
    for so in neighbours:
        story_objects[so.to_storyobject] = so.to_storyobject

    for so in story_objects:
        print(so.name)

    edge_labels = {}

    G = nx.MultiDiGraph()

    for so in story_objects:
        find_colour(so)
        G.add_node(so.name, name=so.name, role=so.role,
            url="http://story-chronicles.herokuapp.com/personas/story_object/{}".format(so.slug),
            node_color=node_colors[so.name], node_shape=node_shapes[so.name])
        labels[so.name] = so.name
        simple_colours.append(node_colors[so.name])

        for i in neighbours:
            source = i.from_storyobject.name
            target = i.to_storyobject.name
            context = i.relationship_class

            if int(i.weight) > 10:
                weight = int(i.weight)/10
            else:
                weight = int(i.weight)

            G.add_edge(source, target, label=context, weight=weight)
            edge_labels[(source, target)] = context

    # Export to JSON format
    from networkx.readwrite import json_graph

    d = json_graph.node_link_data(G)

    # Reset Data
    G = None

    return json.dumps(d)

if __name__ == "__main__":
    return_json_graph("Logos of Ios")