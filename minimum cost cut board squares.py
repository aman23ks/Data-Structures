m = 6
n = 4
X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]

X.sort(reverse=True)
Y.sort(reverse=True)
answer = 0
m = m-1
n = n-1
hr = 1
vt = 1
i = 0
j = 0
while i < m and j < n:
    if X[i] > Y[j]:
        answer += X[i]*vt
        hr += 1
        i += 1
    else:
        answer += Y[j]*hr
        vt += 1
        j += 1

while i < m:
    answer += X[i]*vt
    i += 1
while j < n:
    answer += Y[j]*hr
    j += 1

print(answer)


print(X)
print(Y)
