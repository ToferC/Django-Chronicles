import json
import networkx as nx
import os
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
import django
django.setup()
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models import F, Q

from personas.models import StoryObject, Statistic, Skill, Ability, Aspect, CombatInfo, Relationship

node_shapes = {}
node_colors = {}


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

def return_json_graph(story_objects):

    G = nx.MultiDiGraph()

    for so in story_objects:
        find_colour(so)
        G.add_node(so.name, name=so.name, role=so.role,
            url="http://story-chronicles.herokuapp.com/personas/storyobject/{}".format(so.slug),
            node_color=node_colors[so.name], node_shape=node_shapes[so.name],
            image=so.image.url)

        links = Relationship.objects.filter(
                Q(from_storyobject__name=so.name))

        for i in links:
            if i.to_storyobject in story_objects:
                source = i.from_storyobject.name
                target = i.to_storyobject.name
                context = i.relationship_class

                weight = re.sub(r"\D", "", i.weight)

                if int(weight) > 10:
                    weight = int(weight)/10
                else:
                    weight = int(weight)

                G.add_edge(source, target, label=context, weight=weight)

    # Export to JSON format
    from networkx.readwrite import json_graph

    d = json_graph.node_link_data(G)

    # Reset Data
    G = None

    return json.dumps(d)

if __name__ == "__main__":
    print(return_json_graph(StoryObject.objects.get(name="Logos of Ios")))
