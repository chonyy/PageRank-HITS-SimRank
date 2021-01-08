from src.utils.utils import init_graph
from src.HITS import HITS_one_iter
from src.PageRank import PageRank_one_iter
from src.SimRank import SimRank_one_iter
from src.Similarity import Similarity
import matplotlib.pyplot as plt
import numpy as np
import os

damping_factor = 0.15
decay_factor = 0.9
iteration = 10
file_path = 'dataset/graph_4.txt'
result_dir = 'result'
fname = file_path.split('/')[-1].split('.')[0]

graph = init_graph(file_path)
sim = Similarity(graph, decay_factor)

length = len(graph.nodes)
all_auth = [[] for i in range(length)]
all_hub = [[] for i in range(length)]


for i in range(iteration):
    HITS_one_iter(graph)
    auth_list, hub_list = graph.get_auth_hub_list()
    for idx, auth in enumerate(auth_list):
        all_auth[idx].append(auth)
    for idx, hub in enumerate(hub_list):
        all_hub[idx].append(hub)

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharex=True, figsize=(15, 5))

for auth_list in all_auth:
    ax1.plot(auth_list)

for hub_list in all_hub:
    ax2.plot(hub_list)


ax1.title.set_text('Authority on iteration')
ax1.legend([node.name for node in graph.nodes])
ax1.set(xlabel='Iteration', ylabel='Value')

ax2.title.set_text('Hub on iteration')
ax2.legend([node.name for node in graph.nodes])
ax2.set(xlabel='Iteration', ylabel='Value')

plt.show()
