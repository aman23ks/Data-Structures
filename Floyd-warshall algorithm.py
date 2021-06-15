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
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_vertex(3)
graph.add_vertex(4)
graph.add_edge(2, 1, 8)
graph.add_edge(1, 2, 3)
graph.add_edge(3, 1, 5)
graph.add_edge(1, 4, 7)
graph.add_edge(4, 1, 2)
graph.add_edge(2, 3, 2)
graph.add_edge(3, 4, 1)

print(graph)


def FloydWarshall(graph, edge_list):
    matrix = []
    for i in range(len(graph)):
        val = []
        for j in range(len(graph)):
            val.append(float("inf"))
        matrix.append(val)

    for i in range(len(graph)):
        for j in range(len(graph)):
            if i == j:
                matrix[i][j] = 0
            else:
                try:
                    matrix[i][j] = edge_list[(i+1, j+1)]
                except KeyError:
                    continue

    for k in range(len(graph)):
        for i in range(len(graph)):
            for j in range(len(graph)):
                matrix[i][j] = min(matrix[i][j], matrix[i][k]+matrix[k][j])

    return matrix


print(FloydWarshall(graph.adjancency_list, graph.weight))
