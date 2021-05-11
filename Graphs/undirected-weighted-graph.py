# Undirected weighted graph
class Graph:
    def __init__(self):
        self.adjancency_list = {}
        self.number_of_nodes = 0
        self.weight = {}

    def add_vertex(self, node1):
        self.adjancency_list[node1] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2, weight):
        self.adjancency_list[node1].append(node2)
        self.adjancency_list[node2].append(node1)
        self.weight[node1, node2] = weight

    def __str__(self):
        return f"Edge List: {str(self.weight)} \nAdjancency List: {str(self.adjancency_list)}\nNumber of nodes: {self.number_of_nodes}"


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_edge(0, 1, 7)
graph.add_edge(1, 2, 6)
graph.add_edge(0, 2, 4)
graph.add_edge(1, 3, 4)
graph.add_edge(3, 4, 5)
graph.add_edge(4, 2, 3)
graph.add_edge(4, 5, 4)
graph.add_edge(5, 6, 2)
print(graph)
