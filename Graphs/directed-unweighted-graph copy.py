# Directed unweighted graph
class Graph:
    def __init__(self):
        self.adjancency_list = {}
        self.number_of_nodes = 0

    def add_vertex(self, node1):
        self.adjancency_list[node1] = []
        self.number_of_nodes += 1

    def add_edge(self, node1, node2, isDirected=True):
        if isDirected:
            self.adjancency_list[node1].append(node2)

    def __str__(self):
        return f"Adjancency List: {str(self.adjancency_list)}\nNumber of nodes: {self.number_of_nodes}"


graph = Graph()
graph.add_vertex(0)
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(2, 4)
print(graph)
