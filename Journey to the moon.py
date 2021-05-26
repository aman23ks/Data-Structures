from typing import DefaultDict


astronaut = [[0, 1], [2, 3], [0, 4]]
n = 5
p = 3


def DFS(adj, visited, curr_vector, count):
    visited[curr_vector] = True
    count += 1
    curr_list = adj[curr_vector]
    for i in curr_list:
        if visited[i] == False:
            count = DFS(adj, visited, i, count)
    return count


def journeyToMoon(n, astronaut):
    ans = 0
    adj = DefaultDict(list)
    solution = []
    visited = {}
    for i in range(n):
        visited[i] = False

    for i in range(len(astronaut)):
        adj[astronaut[i][0]].append(astronaut[i][1])
        adj[astronaut[i][1]].append(astronaut[i][0])

    for i in range(n):
        count = 0
        if visited[i] == False:
            value = DFS(adj, visited, i, count)
            solution.append(value)

    val = (n*(n-1))/2

    for i in range(len(solution)):
        ans += (solution[i]*(solution[i]-1))/2

    return val-ans


print(journeyToMoon(n, astronaut))
