from Graph import Node, Graph

with open('dataset/graph_4.txt') as f:
    lines = f.readlines()

graph = Graph()

for line in lines:
    [parent, child] = line.strip().split(',')
    graph.add_edge(parent, child)

graph.display()
