def subArrayExists(arr, n):
    s = 0
    f = 0

    hashmap = {}

    for i in range(n):
        s = s + arr[i]

        if arr[i] == 0 or s in hashmap or s == 0:
            f = 1
            break
        else:
            hashmap[s] = 1

    if f == 1:
        return True
    else:
        return False


arr = [4, 2, -3, 1, 6]
n = len(arr)
print(subArrayExists(arr, n))
