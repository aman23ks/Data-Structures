q = [1, 2, 3, 4, 5]
k = 3

q1 = []
# n = len(q) - k
# for i in range(len(q)-1,n-1,-1):
#     q1.append(q[i])

# q = q[::-1]
# for i in range(len(q1)-1):
#     q.append(q1.pop(0))

# return q.

for i in range(k):
    q1.append(q.pop(0))
    # print(q.pop(0))
    # q.pop(0)
q1 = q1[::-1]

q1 = q1 + q
print(q1)
