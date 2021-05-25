from typing import DefaultDict, List


n = 4
connections = [[0, 1], [0, 2], [1, 2]]


def DFS(adj, visited, curr_vector):
    visited[curr_vector] = True
    curr_list = adj[curr_vector]
    for i in curr_list:
        if visited[i] == False:
            DFS(adj, visited, i)


def makeConnected(n, connections):
    components = 0
    adj = DefaultDict(list)
    visited = {}

    for i in range(n):
        visited[i] = False

    edges = 0

    # Step 1 : Create an adjancency list
    for i in range(len(connections)):
        adj[connections[i][0]].append(connections[i][1])
        adj[connections[i][1]].append(connections[i][0])
        edges += 1
    print(adj)

    # Step 2 : Find number of components using DFS
    for i in range(n):
        if visited[i] == False:
            components += 1
            DFS(adj, visited, i)

    # Step 3 : Count the number of redundant edges
    if edges < n-1:
        return -1
    else:
        redundant_edges = edges - ((n-1)-(components-1))
        if redundant_edges >= components - 1:
            return components-1
        else:
            return -1


print(makeConnected(n, connections))
