N = 8
M = 5
A = [3, 4, 1, 9, 56, 7, 9, 12]

A.sort()

minimum = float("inf")
j = M-1
i = 0
while j < N:
    minimum = min(minimum, A[j]-A[i])
    i += 1
    j += 1

print(minimum)
print(A)
