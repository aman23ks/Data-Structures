def Maxheapify(arr, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i
    if l < n and arr[l] > arr[i]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        Maxheapify(arr, n, largest)


def convertMaxHeap(arr, n):
    for i in range(n // 2, -1, -1):
        Maxheapify(arr, n, i)

    return arr


arr = [3, 5, 9, 6, 8, 20, 10, 12, 18, 9]
n = len(arr)
print(convertMaxHeap(arr, n))
