arr = [5, 20, 3, 2, 5, 80]


N = 78


def findPair(arr):

    arr = sorted(arr)
    l = 0
    r = 1
    while l < len(arr) and r < len(arr):
        if l != r and arr[r] - arr[l] == N:
            return 1

        elif arr[r] - arr[l] < N:
            r += 1

        else:
            l += 1
    return -1


print(findPair(arr))
