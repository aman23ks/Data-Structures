A = ["bella", "label", "roller"]


# def LetterFrequencyCounter(a):
#     letters = {}
#     for i in a:
#         if i not in letters:
#             letters[i] = 1
#         else:
#             letters[i] += 1
#     return letters


# f = []

# for i in A:
#     frequecy = LetterFrequencyCounter(i)
#     f.append(frequecy)

# freq = {}

# for i in f:
#     for key, value in i.items():
#         if key not in freq:
#             freq[key] = 1
#         else:
#             freq[key] += 1


n = len(A)
ans = []
for ele in A[0]:
    i = 0
    while i < n-1:
        if ele not in A[i+1]:
            break
        else:
            lst = list(A[i+1])
            p = lst.index(ele)
            del (lst[p])
            A[i+1] = "".join(lst)
            i += 1

    if i == n-1:
        ans.append(ele)
print(ans)
