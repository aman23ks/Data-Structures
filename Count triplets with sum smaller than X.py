c = 0

arr = [30, 8, 23, 6, 10, 9, 31, 7, 19, 20, 1, 33, 21, 27, 28, 3, 25, 26]
n = len(arr)
sum = 86

arr = sorted(arr)
# print(arr)
# print(n)
for i in range(0, n-2):
    j = i + 1
    k = n - 1
    while j < k:
        s = arr[i] + arr[j] + arr[k]
        # print(s)
        if s < sum:
            c += (k-j)
            # print(c)
            j += 1
        else:
            k -= 1
print(c)
