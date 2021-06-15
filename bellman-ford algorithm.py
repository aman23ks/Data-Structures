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
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_edge(1, 2, 6)
graph.add_edge(1, 3, 5)
graph.add_edge(1, 4, 5)
graph.add_edge(2, 5, -1)
graph.add_edge(3, 2, -2)
graph.add_edge(3, 5, 1)
graph.add_edge(4, 3, -2)
graph.add_edge(4, 6, -1)
graph.add_edge(5, 7, 3)
graph.add_edge(6, 7, 3)

print(graph)


def BellmanFord(graph, edge_list):

    parent = [None]*len(graph)
    value = [float("inf")]*len(graph)

    value[0] = 0
    parent[0] = -1

    edges_list = []

    for i in edge_list:
        edges_list.append([i, edge_list[i]])

    for i in range(len(graph)-1):
        updated = False
        for j in range(len(edges_list)):
            U = edges_list[j][0][0]
            V = edges_list[j][0][1]
            wt = edges_list[j][1]
            if value[U-1] != float("inf") and value[U-1] + wt < value[V-1]:
                value[V-1] = value[U-1] + wt
                parent[V-1] = U
                updated = True

                if updated == False:
                    break

    for i in range(len(edges_list)):
        U = edges_list[j][0][0]
        V = edges_list[j][0][1]
        wt = edges_list[j][1]
        if value[U-1] != float("inf") and value[U-1] + wt < value[V-1]:
            return "Negative cycle present"

        return "Not present"


print(BellmanFord(graph.adjancency_list, graph.weight))
