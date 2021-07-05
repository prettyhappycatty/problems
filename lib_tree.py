class Node:
    def __init__(self, data):
        self.neighbors = []
        self.data = data

nodes = [Node(10), Node(2), Node(3)]

def connect(a, b):
    for i in range(len(nodes)):
        if nodes[i].data == a:
            nodes[i].neighbors.append(b)
        if nodes[i].data == b:
            nodes[i].neighbors.append(a)


connect(10, 3)
for i in range(len(nodes)):
    print(nodes[i].data, nodes[i].neighbors)