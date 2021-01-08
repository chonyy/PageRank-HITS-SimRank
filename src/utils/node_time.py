from src.utils.utils import init_graph
from src.HITS import HITS
from src.PageRank import PageRank
from src.SimRank import SimRank
from src.Similarity import Similarity
from optparse import OptionParser
import numpy as np
import os
import itertools
import random
import time
import matplotlib.pyplot as plt


def create_graph(node_num):
    edges = []
    node_list = [i+1 for i in range(node_num)]
    edge_num = node_num * 2
    edge_pool = list(itertools.permutations(node_list, 2))
    for i in range(edge_num):
        edge = random.choice(edge_pool)
        edges.append(edge)

    with open('dataset/node.txt', 'w') as f:
        for edge in edges:
            f.write(f'{edge[0]},{edge[1]}\n')


# create_graph(10)

time_list = []

for i in range(0, 100, 10):
    print(i)
    create_graph(i)
    graph = init_graph('dataset/node.txt')
    sim = Similarity(graph, 0.9)

    prev_time = time.time()
    SimRank(graph, sim)
    time_list.append(time.time() - prev_time)

x = [2*i for i in range(0, 100, 10)]

plt.plot(x, time_list)
plt.title('SimRank computation time with different number of edges')
plt.xlabel('Edges')
plt.ylabel('Time (sec)')
plt.show()
