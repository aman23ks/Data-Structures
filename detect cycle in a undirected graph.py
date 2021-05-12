# Graphs are data structures which contain nodes or vertices, which are connected to each other through edges.
# Tress and Linked Lists are basically graphs having nodes and connections between the nodes.
# Now, graphs are primarily classified by three properties - Cyclic/Acyclic, Weighted/Unweighted/, Directed/Undirected Graphs
# There are many many applications of graphs and many opertions can be performed on them.
# A graph can be represented in 3 ways - Adjacency List, Adjacency Matrix, Edge List.
# Adjacency list stores the nodes with which a particular node is connected to in a linked list or array.
# All these lists or arrays can be stored in a hash table with the keys being the nodes and the values being their respective lists
# Adjcaency matrix is a nXn matrix where n is the number of nodes. M[i][j] = 1 if nodes i and j are connected otherwise 0
# Edge list contains all the pairs of nodes which are connected, and if the graph is weighted, then the weight of each edge as well
# Here we will build an undirected graph using an adjacency list.

class Graph():

    # The constructior will initialize the number of vertices in the graph to zero and the adjcency list to an empty dictionary
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacentList = {}


# Now we will implement the insert node method.
# We will add the value of the node as a key in the adjacency list and initialize the value of the key to be an empty array

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.number_of_nodes += 1


# Next we will implement the insert edge method where we will specify two nodes between which an edge is to be added.
# First we will check if an edge already exists by checking the adjacency list of either of the two nodes.
# If the other node is present it means the edge already exists, if not then the edge doesn't exist.
# So we add the edge by adding the complimentary node in the adjacency list of either node

    def addEdge(self, node1, node2):
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)


# Finally we will implement a custom print method which willl print the nodes and their connections

    def __str__(self):
        return str(self.adjacentList)


myGraph = Graph()
myGraph.addVertex(0)
myGraph.addVertex(1)
myGraph.addVertex(2)
myGraph.addVertex(3)
myGraph.addVertex(4)
myGraph.addVertex(5)
myGraph.addVertex(6)
myGraph.addVertex(7)
myGraph.addEdge(0, 4)
myGraph.addEdge(0, 5)
myGraph.addEdge(0, 6)
myGraph.addEdge(0, 7)
myGraph.addEdge(1, 2)
myGraph.addEdge(1, 4)
myGraph.addEdge(2, 3)
myGraph.addEdge(2, 6)
myGraph.addEdge(2, 7)
myGraph.addEdge(3, 4)
myGraph.addEdge(3, 5)
myGraph.addEdge(3, 7)
myGraph.addEdge(4, 5)
myGraph.addEdge(6, 7)
print(myGraph)


def cycle_exists(G):
    marked = {u: False for u in G}
    found_cycle = [False]

    for u in G:
        if not marked[u]:
            dfs_visit(G, u, found_cycle, u, marked)
        if found_cycle[0]:
            break
    return found_cycle[0]


def dfs_visit(G, u, found_cycle, pred_node, marked):
    if found_cycle[0]:
        return
    marked[u] = True
    print(marked)
    for v in G[u]:
        print(pred_node, v)
        if marked[v] and v != pred_node:

            found_cycle[0] = True
            return
        if not marked[v]:
            dfs_visit(G, v, found_cycle, u, marked)


print(cycle_exists(myGraph.adjacentList))
