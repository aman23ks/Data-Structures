n = [-1, 2, -3, 4, 5, 6, -7, 8, 9]

j = 0
for i in range(len(n)):
    if n[i] < 0:
        temp = n[i]
        n[i] = n[j]
        n[j] = temp
        j = j + 1

print(n)
