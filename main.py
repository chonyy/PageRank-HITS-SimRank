from src.utils import init_graph
from src.HITS import HITS
from src.PageRank import PageRank
from src.SimRank import SimRank
from src.Similarity import Similarity
import numpy as np
import os


def output_HITS(iteration, graph, result_dir, fname):
    authority_fname = '_HITS_authority.txt'
    hub_fname = '_HITS_hub.txt'

    HITS(iteration, graph)
    auth_list, hub_list = graph.get_auth_hub_list()
    print()
    print('Authority:')
    print(auth_list)
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + authority_fname), auth_list, fmt='%.3f', newline=" ")
    print('Hub:')
    print(hub_list)
    print()
    np.savetxt(os.path.join(path, fname + hub_fname), hub_list, fmt='%.3f', newline=" ")


def output_PageRank(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = '_PageRank.txt'

    PageRank(iteration, graph, damping_factor)
    pagerank_list = graph.get_pagerank_list()
    print('PageRank:')
    print(pagerank_list)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + pagerank_fname), pagerank_list, fmt='%.3f', newline=" ")


def output_SimRank(iteration, graph, decay_factor, result_dir, fname):
    simrank_fname = '_SimRank.txt'

    SimRank(iteration, graph, sim)
    ans = sim.get_sim_matrix()
    print('SimRank:')
    print(ans)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + simrank_fname), ans, delimiter=' ', fmt='%.3f')


if __name__ == '__main__':
    damping_factor = 0.15
    decay_factor = 0.9
    iteration = 500
    file_path = 'dataset/IBM.txt'
    result_dir = 'result'
    fname = file_path.split('/')[-1].split('.')[0]

    graph = init_graph(file_path)
    sim = Similarity(graph, decay_factor)

    output_HITS(iteration, graph, result_dir, fname)
    output_PageRank(iteration, graph, damping_factor, result_dir, fname)
    output_SimRank(iteration, graph, decay_factor, result_dir, fname)
