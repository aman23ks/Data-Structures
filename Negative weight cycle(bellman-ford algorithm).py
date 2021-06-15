def isNegativeWeightCycle(n, edges):

    values = [float("inf")]*n
    values[0] = 0
    for i in range(n-1):
        updated = False
        for j in range(len(edges)):
            U = edges[j][0]
            V = edges[j][1]
            wt = edges[j][2]
            if values[U] != float("inf") and values[U] + wt < values[V]:
                values[V] = values[U] + wt
                updated = True

                if updated == False:
                    break

    for j in range(len(edges)):
        U = edges[j][0]
        V = edges[j][1]
        wt = edges[j][2]
        if values[U] != float("inf") and values[U] + wt < values[V]:
            return 1

    return 0


print(isNegativeWeightCycle(3, [[0, 1, -1], [1, 2, -2], [2, 0, -3]]))
