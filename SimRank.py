from Graph import Node, Graph
from Similarity import Similarity
from utils import init_graph
import numpy as np


def SimRank_one_iter(graph, sim):
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            new_SimRank = sim.calculate_SimRank(node1, node2)
            sim.update_sim_value(node1, node2, new_SimRank)
            # print(node1.name, node2.name, new_SimRank)

    sim.replace_sim()


def SimRank(iteration, graph, sim):
    for i in range(iteration):
        SimRank_one_iter(graph, sim)
        ans = sim.get_sim_matrix()
        print(ans)
        print()


if __name__ == '__main__':

    decay_factor = 0.8
    iteration = 5

    graph = init_graph('dataset/simrank.txt')
    sim = Similarity(graph, decay_factor)

    SimRank(iteration, graph, sim)
