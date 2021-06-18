# Topological sort works for directed acyclic graphs

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
graph.add_vertex(5)
graph.add_vertex(6)
graph.add_vertex(7)
graph.add_vertex(8)
graph.add_vertex(9)
graph.add_vertex(10)
graph.add_vertex(11)
graph.add_vertex(12)
graph.add_edge(2, 0)
graph.add_edge(2, 1)
graph.add_edge(0, 3)
graph.add_edge(1, 3)
graph.add_edge(4, 0)
graph.add_edge(4, 3)
graph.add_edge(4, 5)
graph.add_edge(3, 7)
graph.add_edge(3, 6)
graph.add_edge(7, 8)
graph.add_edge(6, 8)
graph.add_edge(5, 10)
graph.add_edge(5, 9)
graph.add_edge(7, 9)
graph.add_edge(10, 9)
graph.add_edge(9, 12)
graph.add_edge(9, 11)
graph.add_edge(8, 11)
print(graph)


def dfs(graph, visited, i, sorted_array):
    visited[i] = True
    for j in range(len(graph[i])):
        if visited[graph[i][j]] == False:
            dfs(graph, visited, graph[i][j], sorted_array)
    sorted_array.append(i)


def TopologicalSort(graph):
    sorted_array = []
    visited = [False]*len(graph)
    for i in range(len(graph)):
        if visited[i] == False:
            dfs(graph, visited, i, sorted_array)

    return sorted_array[::-1]


print(TopologicalSort(graph.adjancency_list))
