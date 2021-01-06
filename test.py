import networkx as nx
import numpy as np
from numpy import array
from utils import init_graph
import matplotlib.pyplot as plt

with open('./dataset/graph_4.txt') as f:
    lines = f.readlines()

G = nx.DiGraph()

for line in lines:
    t = tuple(line.strip().split(','))
    G.add_edge(*t)

# pr = nx.pagerank(G)
# pr = dict(sorted(pr.items(), key=lambda x: x[0]))
# print(np.round(list(pr.values()), 2))


# h, a = nx.hits(G, max_iter=100)
# h = dict(sorted(h.items(), key=lambda x: x[0]))
# a = dict(sorted(a.items(), key=lambda x: x[0]))

# print(np.round(list(a.values()), 2))
# print(np.round(list(h.values()), 2))


sim = nx.simrank_similarity(G)
lol = [[sim[u][v] for v in sorted(sim[u])] for u in sorted(sim)]
sim_array = np.round(array(lol), 2)
print(sim_array)

# nx.draw(G, with_labels=True)
# plt.savefig("graph.png")
