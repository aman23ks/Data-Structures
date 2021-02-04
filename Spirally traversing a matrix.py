R = 4
C = 4
mat_list = []
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
for i in range(R):
    for j in range(C):
        if j == C:
            mat_list.append(matrix[i][j])
        else:
            mat_list.append(matrix[i][j])

print(mat_list)
