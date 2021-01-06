import copy
import numpy as np


class Similarity:
    def __init__(self, graph, decay_factor):
        self.decay_factor = decay_factor
        self.name_list, self.old_sim = self.init_sim(graph)
        self.node_num = len(self.name_list)
        self.new_sim = [[0] * self.node_num for i in range(self.node_num)]

    def init_sim(self, graph):
        nodes = graph.nodes
        name_list = [node.name for node in nodes]
        sim = []
        for name1 in name_list:
            temp_sim = []
            for name2 in name_list:
                if(name1 == name2):
                    temp_sim.append(1)
                else:
                    temp_sim.append(0)
            sim.append(temp_sim)

        return name_list, sim

    def get_name_index(self, name):
        return (self.name_list.index(name))

    def get_sim_value(self, node1, node2):
        node1_idx = self.get_name_index(node1.name)
        node2_idx = self.get_name_index(node2.name)
        return self.old_sim[node1_idx][node2_idx]

    def replace_sim(self):
        self.old_sim = copy.deepcopy(self.new_sim)

    def calculate_SimRank(self, node1, node2):
        # Return 1 if it's same node
        if(node1.name == node2.name):
            return 1.0

        in_neighbors1 = node1.parents
        in_neighbors2 = node2.parents

        # Return 0 if one of them has no in-neighbor
        if(len(in_neighbors1) == 0 or len(in_neighbors2) == 0):
            return 0.0

        SimRank_sum = 0
        for in1 in in_neighbors1:
            for in2 in in_neighbors2:
                SimRank_sum += self.get_sim_value(in1, in2)

        # Follows the equation
        scale = self.decay_factor / (len(in_neighbors1) * len(in_neighbors2))
        new_SimRank = scale * SimRank_sum

        return new_SimRank

    def update_sim_value(self, node1, node2, value):
        node1_idx = self.get_name_index(node1.name)
        node2_idx = self.get_name_index(node2.name)
        self.new_sim[node1_idx][node2_idx] = value

    def get_sim_matrix(self):
        return np.round(np.asarray(self.new_sim), 3)
