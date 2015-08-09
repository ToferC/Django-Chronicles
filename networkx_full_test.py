import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

nodes = "1 2 3 4 5 6 7 8 9".split(" ")
previous = "None 1 2 3 4 5 6 7 8".split(" ")

scenes = []
labels = []

for i in range(len(nodes)):
    scenes.append([nodes[i], previous[i]])

print(scenes)

target = None

# Find first scene
for scene in scenes:
    if scene[1] == 'None': #parallel of previous == None - get first scene
        G.add_node(scene[0])
        labels.append(scene[0])
        target = scene[0]
    else:
        pass

def chain_scenes(scenes, target):
    for scene in scenes:
        if scene[1] == target:
            G.add_edge(target, scene[0])
            labels.append(scene[0])
            target = scene[0]
            chain_scenes(scenes, target)
        else:
            pass

chain_scenes(scenes, target)

srt = nx.topological_sort(G)
print(srt)

pos = nx.spectral_layout(G)

nx.draw_networkx_nodes(G, pos)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos)
plt.show()
