# grid = [[2, 1, 0, 2],
#         [1, 0, 1, 2],
#         [1, 0, 0, 1]]

grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
row = len(grid)
column = len(grid[0])
fresh = 0
t = 0
rotten = []
for i in range(row):
    for j in range(column):
        if grid[i][j] == 2:
            rotten.append([i, j])
        elif grid[i][j] == 1:
            fresh += 1

while len(rotten) > 0:
    for i in range(len(rotten)):
        x, y = rotten[0]
        print(rotten)
        rotten.pop(0)
        lst = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]
        for r, c in lst:
            if r >= 0 and c >= 0 and r < row and c < column and grid[r][c] == 1:
                print(fresh)
                grid[r][c] = 2
                fresh -= 1
                rotten.append([r, c])
                # print(rotten)
    if len(rotten) > 0:
        t += 1
        print("t", t)
        print(rotten)

if fresh == 0:
    print(t)
else:
    print(-1)
