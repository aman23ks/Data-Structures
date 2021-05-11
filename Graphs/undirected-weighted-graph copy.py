# Directed weighted graph
class Graph:
    def __init__(self):
        self.adjancency_list = {}
        self.number_of_nodes = 0
        self.weight = {}

    def add_vertex(self, node1):
        self.adjancency_list[node1] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2, weight, isDirected=True):
        if isDirected:
            self.adjancency_list[node1].append(node2)
        self.weight[node1, node2] = weight

    def __str__(self):
        return f"Edge List: {str(self.weight)} \nAdjancency List: {str(self.adjancency_list)}\nNumber of nodes: {self.number_of_nodes}"


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(0, 1, 99)
graph.add_edge(1, 2, 50)
graph.add_edge(0, 2, 50)
graph.add_edge(1, 3, 50)
graph.add_edge(3, 4, 75)
graph.add_edge(2, 3, 99)
graph.add_edge(1, 4, 50)

print(graph)
