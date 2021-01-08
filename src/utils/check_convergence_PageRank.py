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
all_pagerank = [[] for i in range(length)]


for i in range(iteration):
    PageRank_one_iter(graph, damping_factor)
    pagerank_list = graph.get_pagerank_list()
    for idx, auth in enumerate(pagerank_list):
        all_pagerank[idx].append(auth)

for pagerank_list in all_pagerank:
    plt.plot(pagerank_list)

plt.title('PageRank on iteration')
plt.legend([node.name for node in graph.nodes])
plt.xlabel('Iteration')
plt.ylabel('Value')

plt.show()
