import json
import networkx as nx
import os
import re

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
import django
django.setup()

from django.db.models import F, Q

from personas.models import StoryObject, Relationship

node_shapes = {}
node_colors = {}
node_model = {}


def find_colour(story_object):
    if story_object.c_type == "Character":
        node_shapes[story_object.name] = 'square' # o
        node_colors[story_object.name] = 'r'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Organization":
        node_shapes[story_object.name] = 'circle'
        node_colors[story_object.name] = 'b'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Creature":
        node_shapes[story_object.name] = 'triangle-up' #^
        node_colors[story_object.name] = 'g'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Faction":
        node_shapes[story_object.name] = 'circle' #v
        node_colors[story_object.name] = 'c'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Thing":
        node_shapes[story_object.name] = 'triangle-down' #s
        node_colors[story_object.name] = 'y'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Place":
        node_shapes[story_object.name] = 'diamond' #^
        node_colors[story_object.name] = 'v'
        node_model[story_object.name] = 'place'
    elif story_object.c_type == "Territory":
        node_shapes[story_object.name] = 'cross' #o
        node_colors[story_object.name] = 'o'
        node_model[story_object.name] = 'storyobject'
    elif story_object.c_type == "Event":
        node_shapes[story_object.name] = 'o'
        node_colors[story_object.name] = 'w'
        node_model[story_object.name] = 'storyobject'


def return_json_graph(story_objects):

    G = nx.MultiDiGraph()

    for so in story_objects:

        links = Relationship.objects.filter(
                Q(from_storyobject__name=so.name))

        size = 0

        for i in links:
            if so == i.to_storyobject:
                size += 10

        find_colour(so)
        G.add_node(so.name, id=so.name, role=so.role,
            url="http://story-chronicles.herokuapp.com/personas/{}/{}".format(node_model[so.name], so.slug),
            node_color=so.c_type, type=node_shapes[so.name],
            # image=so.thumbnail.url,
            size=size)

        for i in links:
            if i.to_storyobject in story_objects:
                source = i.from_storyobject.name
                target = i.to_storyobject.name
                context = i.relationship_class

                weight = re.sub(r"\D", "", i.weight)

                if type(weight) == int:
                    if int(weight) > 10:
                        weight = int(weight)/10
                    else:
                        weight = int(weight)
                else:
                    weight = 1

                G.add_edge(source, target, label=context, weight=weight)

    # Export to JSON format
    from networkx.readwrite import json_graph

    d = json_graph.node_link_data(G)

    # Reset Data
    G = None

    return json.dumps(d)

if __name__ == "__main__":
    print(return_json_graph(StoryObject.objects.get(name="Logos of Ios")))
