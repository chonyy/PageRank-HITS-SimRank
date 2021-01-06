import numpy as np


class Graph:
    def __init__(self):
        self.nodes = []

    def contains(self, name):
        for node in self.nodes:
            if(node.name == name):
                return True
        return False

    # Return the node with the name, create and return new node if not found
    def find(self, name):
        if(not self.contains(name)):
            new_node = Node(name)
            self.nodes.append(new_node)
            return new_node
        else:
            return next(node for node in self.nodes if node.name == name)

    def add_edge(self, parent, child):
        parent_node = self.find(parent)
        child_node = self.find(child)

        parent_node.link_child(child_node)
        child_node.link_parent(parent_node)

    def display(self):
        for node in self.nodes:
            print(f'{node.name} links to {[child.name for child in node.children]}')

    def sort_nodes(self):
        self.nodes.sort(key=lambda node: int(node.name))

    def display_hub_auth(self):
        for node in self.nodes:
            print(f'{node.name}  Auth: {node.old_auth}  Hub: {node.old_hub}')

    def normalize_auth_hub(self):
        auth_sum = sum(node.new_auth for node in self.nodes)
        hub_sum = sum(node.new_hub for node in self.nodes)

        for node in self.nodes:
            node.new_auth /= auth_sum
            node.new_hub /= hub_sum

    def get_auth_hub_list(self):
        auth_list = np.asarray([node.new_auth for node in self.nodes], dtype='float32')
        hub_list = np.asarray([node.new_hub for node in self.nodes], dtype='float32')

        return np.round(auth_list, 2), np.round(hub_list, 2)


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []
        self.old_auth = 1.0
        self.old_hub = 1.0
        self.new_auth = 0.0
        self.new_hub = 0.0

    def link_child(self, child):
        self.children.append(child)

    def link_parent(self, parent):
        self.parents.append(parent)

    def replace_auth_hub(self):
        self.old_auth = self.new_auth
        self.old_hub = self.new_hub

    def update_auth(self):
        self.new_auth = sum(node.old_hub for node in self.parents)

    def update_hub(self):
        self.new_hub = sum(node.old_auth for node in self.children)
