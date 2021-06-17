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
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 4)
graph.add_edge(4, 5)
graph.add_edge(5, 6)
graph.add_edge(6, 7)
graph.add_edge(4, 7)
graph.add_edge(6, 4)

print(graph)


def dfs1(visited, graph, i, stack):
    visited[i] = True
    for j in graph[i]:
        if visited[j] == False:
            dfs1(visited, graph, j, stack)

    stack.append(i)


def dfs2(node, visited, new_graph):
    visited[node] = True
    for i in new_graph[node]:
        if visited[i] == False:
            dfs2(i, visited, new_graph)


def reverse(new_adj, n, graph):
    for i in range(n):
        if i not in new_adj:
            new_adj[i] = []

    for i in graph:
        for j in graph[i]:
            new_adj[j].append(i)

    return new_adj


def Kosaraju(graph):

    visited = [False]*len(graph)
    stack = []
    new_adj = {}

    for i in range(len(visited)):
        if visited[i] == False:
            dfs1(visited, graph, i, stack)

    visited = [False]*len(graph)

    new_graph = reverse(new_adj, len(graph), graph)
    count = 0

    while stack != []:
        node = stack.pop()
        if visited[node] == False:
            count += 1
            dfs2(node, visited, new_graph)

    return count


print(
    f"The number of strongly connected components are: {Kosaraju(graph.adjancency_list)}")
