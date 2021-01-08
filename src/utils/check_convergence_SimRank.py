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
iteration = 20
file_path = 'dataset/graph_4.txt'
result_dir = 'result'
fname = file_path.split('/')[-1].split('.')[0]

graph = init_graph(file_path)
sim = Similarity(graph, decay_factor)

length = len(graph.nodes)
all_simrank = [[] for i in range(length)]


for i in range(iteration):
    SimRank_one_iter(graph, sim)
    SimRank_list = sim.get_sim_matrix()[0]
    for idx, auth in enumerate(SimRank_list):
        all_simrank[idx].append(auth)

for SimRank_list in all_simrank:
    plt.plot(SimRank_list)

plt.title('SimRank on iteration')
plt.legend([f'SimRank(1, {node.name})' for node in graph.nodes])
plt.xlabel('Iteration')
plt.ylabel('Value')

plt.show()
