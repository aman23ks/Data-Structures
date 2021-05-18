q = [1, 2, 3, 4, 5]
k = 3

q1 = []

for i in range(k):
    q1.append(q.pop(0))

q1 = q1[::-1]

q1 = q1 + q
print(q1)
