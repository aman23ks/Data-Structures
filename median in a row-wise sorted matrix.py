matrix = [[1, 3, 5],
          [2, 6, 9],
          [3, 6, 9]]

if len(matrix) == 1:
    vec = matrix[0]
    print(vec[len(vec)//2])
else:
    values = []
    for row in range(len(matrix)):
        values.extend(matrix[row])
    values = sorted(values)
    print(values[len(values)//2])
