def findSubArrays(arr):
    hashmap = {0: 1}

    sum = 0
    ans = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum not in hashmap:
            hashmap[sum] = 1
        else:
            ans += hashmap[sum]
            hashmap[sum] += 1

    return ans
