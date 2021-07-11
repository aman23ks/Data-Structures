a = [3, 2, 1]
b = [2, 1, 3]

a.sort()
b.sort()
sum = 0
for i in range(len(a)):
    sum += (abs(a[i]-b[i]))

print(sum)