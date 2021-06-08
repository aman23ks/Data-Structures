arr1 = [1, 10, 10, 25, 40, 54, 79]
arr2 = [15, 24, 27, 32, 33, 39, 48, 68, 82, 88, 90]
k = 15

m = len(arr1)
n = len(arr2)


def KthElement(arr1, arr2, m, n):
    i = 0
    j = 0
    x = 0

    while i < m and j < n:

        if arr1[i] > arr2[j]:
            x += 1
            if x == k:
                return arr2[j]
            j += 1

        elif arr1[i] < arr2[j]:
            x += 1
            if x == k:
                return arr1[i]
            i += 1

        else:
            x += 1
            if x == k:
                return arr1[i]
            i += 1
            j += 1

    while i < m:
        x += 1
        if x == k:
            return arr1[i]
        i += 1

    while j < n:
        x += 1
        if x == k:
            return arr2[j]
        j += 1


print(KthElement(arr1, arr2, m, n))
