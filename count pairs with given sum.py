def getPairsCount(arr, n, k):
    hashmap = {}
    count = 0
    for i in range(n):

        x = k - arr[i]

        if x not in hashmap:
            hashmap[arr[i]] = 1
        else:
            count += hashmap[x]
            if arr[i] not in hashmap:
                hashmap[arr[i]] = 1
            else:
                hashmap[arr[i]] += 1
    # print(hashmap)
    return count


arr = [9, 7, 53, 41, 4, 97, 75, 30, 54, 61, 9, 8, 14, 50, 95, 38, 12, 38, 44, 2, 78,
       71, 97, 67, 10, 4, 68, 43, 47, 56, 35, 7, 62, 39, 47, 17, 36, 21, 46, 41, 34, 7]
n = len(arr)
k = 43

print(getPairsCount(arr, n, k))
