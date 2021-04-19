Mat = [[10, 20, 30, 40],
       [15, 25, 35, 45],
       [27, 29, 37, 48],
       [32, 33, 39, 50]]

values = []
new_row_list = []
new_mat = []
count = 0
j = 0
N = 4
for row in range(len(Mat)):
    values.extend(Mat[row])
values = sorted(values)
# print(values)
for i in range(N*N):
    for j in range(N):
        if j == (N-1):
            break
        new_row_list.append(values[i])
    new_mat.append(new_row_list)
    new_row_list = []

print(new_mat)
