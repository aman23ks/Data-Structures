# m = [[1, 0, 0, 0],
#      [1, 1, 0, 1],
#      [1, 1, 0, 0],
#      [0, 1, 1, 1]]

m = [[1, 1, 1], [1, 1, 0], [1, 1, 1]]

# m = [[1, 0],
#      [1, 0]]

v = []


def dfs(r, c, m, n, s, vis):
    if r < 0 or c < 0 or r >= n or c >= n:
        return
    if m[r][c] == 0 or vis[r][c] == 1:
        return
    if r == n-1 and c == n-1:
        v.append(s)
        return
    vis[r][c] = 1

    dfs(r-1, c, m, n, s+"U", vis)
    dfs(r+1, c, m, n, s+"D", vis)
    dfs(r, c-1, m, n, s+"L", vis)
    dfs(r, c+1, m, n, s+"R", vis)

    # Step for Backtracking
    vis[r][c] = 0

    return


def findPath(m, n):
    if m[n-1][n-1] == 0 or m[0][0] == 0:
        return v

    vis = []
    for i in range(n):
        level = []
        for j in range(n):
            level.append(0)
        vis.append(level)

    s = ""

    dfs(0, 0, m, n, s, vis)

    sorted(v)

    return v


print(findPath(m, len(m)))
