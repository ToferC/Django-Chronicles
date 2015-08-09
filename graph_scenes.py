import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'persona2.settings')
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

import django
import networkx as nx
from networkx.readwrite import json_graph
import matplotlib.pyplot as plt
django.setup()

from personas.models import Chapter, Scene, Story

s = Story.objects.get(slug="roma-britannica")

chapter = Chapter.objects.filter(story__slug="roma-britannica")[6]

scenes = Scene.objects.filter(chapter=chapter)

G = nx.DiGraph()

#G.add_node(chapter.title)

target = None

for scene in scenes:
    if scene.order == 1: #parallel of previous == None - get first scene
        G.add_node(scene)
        target = scene
    else:
        pass

def chain_scenes(scenes, target):
    for scene in scenes:
        if scene.order == target.order + 1:
            G.add_edge(target, scene)
            target = scene
            chain_scenes(scenes, target)
        else:
            pass

chain_scenes(scenes, target)

'''
        print(scene)
        G.add_node(scene.title)

    if connect_node:
        G.add_edge(scene.title, connect_node)
    else:
        pass

    connect_node = scene.title
'''
srt = nx.topological_sort(G)
print(srt)

#nx.write_dot(G, 'test.dot')

#plt.title("Scene Tree Test")
#pos = nx.graphviz_layout(G, prog='dot')
#nx.draw(G, pos, with_labels=False, arrows=False)

#nx.line_graph(G)
#nx.draw(G)
#plt.savefig('nx_test.png')


#nx.draw_networkx_nodes(G, pos)
#nx.draw_networkx_labels(G, pos)
#nx.draw_networkx_edges(G, pos)
#plt.show()

#data = json_graph.node_link_data(G)

#import json

#json.dump(data, open('scenes.json','w'))
#print('Wrote node-link JSON data to force/force.json')
