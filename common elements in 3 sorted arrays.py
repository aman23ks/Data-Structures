def commonElements(A, B, C, n1, n2, n3):

    i = 0
    j = 0
    k = 0
    v = []
    while i < n1-1 and j < n2-1 and k < n3-1:
        if A[i] == B[j] == C[k]:
            if A[i] not in v:
                v.append(A[i])
            i += 1
            j += 1
            k += 1
        elif A[i] < B[j]:
            i += 1
        elif B[j] < C[k]:
            j += 1
        else:
            k += 1

    return v


A = [3, 3, 3]
B = [3, 3, 3]
C = [3, 3, 3]
n1 = len(A)
n2 = len(B)
n3 = len(C)
print(commonElements(A, B, C, n1, n2, n3))
