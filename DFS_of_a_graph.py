# directed unweighted graph
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
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.add_edge("B", "D")
graph.add_edge("B", "E")
graph.add_edge("E", "F")
graph.add_edge("C", "B")
graph.add_edge("C", "F")

print(graph)

stack = [list(graph.adjancency_list.keys())[0]]
DFS_list = []


while stack:
    current = stack.pop()

    for neighbours in graph.adjancency_list[current]:
        if neighbours not in DFS_list:
            stack.append(neighbours)
    DFS_list.append(current)

print(DFS_list[:-1])
