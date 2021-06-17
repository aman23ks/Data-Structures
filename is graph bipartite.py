graph = [[1, 3], [0, 2], [1, 3], [0, 2]]


def isBipartite(graph):
    color = [0]*len(graph)
    for i in range(len(graph)):
        if color[i] == 0:
            q = []
            q.append(i)
            color[i] = 1
            while q != []:
                node = q.pop(0)
                for n in graph[node]:
                    if color[n] == color[node]:
                        return False
                    elif color[n] == 0:
                        q.append(n)
                        color[n] = -color[node]
    return True


print(isBipartite(graph))
