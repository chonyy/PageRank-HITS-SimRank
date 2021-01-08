from src.Graph import Node, Graph
from src.Similarity import Similarity
from src.utils.utils import init_graph
import numpy as np


def SimRank_one_iter(graph, sim):
    for node1 in graph.nodes:
        for node2 in graph.nodes:
            new_SimRank = sim.calculate_SimRank(node1, node2)
            sim.update_sim_value(node1, node2, new_SimRank)
            # print(node1.label, node2.label, new_SimRank)

    sim.replace_sim()


def SimRank(graph, sim, iteration=100):
    for i in range(iteration):
        SimRank_one_iter(graph, sim)
        # ans = sim.get_sim_matrix()
        # print(ans)
        # print()


if __name__ == '__main__':

    decay_factor = 0.9
    iteration = 100

    graph = init_graph('dataset/graph_4.txt')
    sim = Similarity(graph, decay_factor)

    SimRank(iteration, graph, sim)
    ans = sim.get_sim_matrix()
    print(ans)

    np.savetxt('SimRank.txt', ans, delimiter=' ', fmt='%.2f')
