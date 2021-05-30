def find3Numbers(A, n, X):
    # Your Code Here
    A = sorted(A)
    ans = 0
    for i in range(n-2):
        l = i+1
        r = n-1
        while l < r:
            if A[i] + A[l] + A[r] == X:
                ans = 1
                break
            else:
                if A[i] + A[l] + A[r] < X:
                    l += 1
                else:
                    r -= 1
        if ans == 1:
            break
    return ans


A = [1, 2, 4, 3, 6]
n = len(A)
X = 10
print(find3Numbers(A, n, X))
