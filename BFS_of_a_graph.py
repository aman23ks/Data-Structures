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

queue = [list(graph.adjancency_list.keys())[0]]
# list(graph.adjancency_list.keys())[0] - done for getting forst element in the adjancency list
BFS_list = []

while queue:
    val = queue.pop(0)
    BFS_list.append(val)

    if graph.adjancency_list[val]:
        for i in graph.adjancency_list[val]:
            queue.append(i)
print(BFS_list)
