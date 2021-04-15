matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]

rowbegin = 0
rowend = len(matrix)
columnbegin = 0
columnend = len(matrix[0])
res = []

while columnbegin < columnend and rowbegin < rowend:
    for i in range(rowbegin, rowend):
        res.append(matrix[i][columnbegin])
    columnbegin += 1

res = sorted(res)
print(res[len(res)//2])
