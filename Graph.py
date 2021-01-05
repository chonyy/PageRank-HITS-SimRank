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
            print(
                f'{node.name} links to {[child.name for child in node.children]}')


class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def link_child(self, child):
        self.children.append(child)

    def link_parent(self, parent):
        self.parents.append(parent)
