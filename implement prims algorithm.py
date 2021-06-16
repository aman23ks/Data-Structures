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
graph.add_edge(0, 1, 4)
graph.add_edge(1, 2, 6)
graph.add_edge(0, 2, 6)
graph.add_edge(1, 3, 3)
graph.add_edge(3, 4, 2)
graph.add_edge(3, 2, 1)
graph.add_edge(3, 5, 3)
graph.add_edge(4, 1, 4)
graph.add_edge(4, 5, 7)
print(graph)


def MinVertex(processed, values):
    minimum = float("inf")
    vertex = 0
    for i in range(len(processed)):
        if processed[i] == False and values[i] < minimum:
            minimum = values[i]
            vertex = i
    return vertex


def check(processed, values, parent, edge, graph, U, j):
    if edge != 0 and processed[graph[U][j]] == False and edge < values[graph[U][j]]:
        values[graph[U][j]] = edge
        parent[graph[U][j]] = U


def Prims(graph, edge_list):
    parent = [None]*len(graph)
    processed = [False]*len(graph)
    values = [float("inf")]*len(graph)

    values[0] = 0
    parent[0] = -1

    for i in range(len(graph)-1):
        U = MinVertex(processed, values)
        processed[U] = True
        for j in range(len(graph[U])):
            try:
                check(processed, values, parent,
                      edge_list[(U, graph[U][j])], graph, U, j)
            except KeyError:
                check(processed, values, parent,
                      edge_list[(graph[U][j], U)], graph, U, j)

    return values


print(Prims(graph.adjancency_list, graph.weight))
