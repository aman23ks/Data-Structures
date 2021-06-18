n = 6
KnightPos = [4, 5]
TargetPos = [1, 1]

# n = 7
# KnightPos = [6, 1]
# TargetPos = [2, 4]

# n = 3
# KnightPos = [3, 3]
# TargetPos = [2, 1]


def MinimumStepKnight(KnightPos, TargetPos, n):
    x1 = KnightPos[0]
    y1 = KnightPos[1]
    x2 = TargetPos[0]
    y2 = TargetPos[1]

    if x1 == x2 and y1 == y2:
        return 0

    a = []
    for i in range(n):
        value = []
        for j in range(n):
            value.append(0)
        a.append(value)

    q = []
    # this is done because the values are in 1 based index and we need to do 0 based indexing
    q.append([x1-1, y1-1])
    while q != []:
        curr = q.pop(0)
        i = curr[0]
        j = curr[1]
        # If the position is already visited don't go to that place
        lst = [[i+1, j+2], [i+2, j+1], [i-1, j-2], [i-2, j-1],
               [i+1, j-2], [i+2, j-1], [i-2, j+1], [i-1, j+2]]
        for r, c in lst:
            if a[x2-1][y2-1] > 0:
                return a[x2-1][y2-1]
            else:
                if r >= 0 and r < n and c >= 0 and c < n and a[r][c] == 0:
                    a[r][c] = a[i][j] + 1
                    q.append([r, c])
    return a[x2-1][y2-1]


print(MinimumStepKnight(KnightPos, TargetPos, n))
