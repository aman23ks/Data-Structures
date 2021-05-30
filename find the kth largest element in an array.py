def heapify(arr, n, i):
    l = 2*i + 1
    r = 2*i + 2

    largest = i
    if l < n and arr[l] < arr[i]:
        largest = l
    if r < n and arr[r] < arr[i]:
        largest = r

    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]

        heapify(arr, n, largest)


def kthLargest(arr, size, k):
    min_heap = []
    for i in range(k):
        min_heap.append(arr[i])

    for i in range(k, size):
        # min_heap.sort()
        # print(min_heap)
        heapify(arr, k, i)

        if arr[i] > arr[0]:
            min_heap.pop(0)
            min_heap.append(arr[i])
            heapify(arr, k, i)
        else:
            continue

    return min_heap


nums = [3, 2, 1, 5, 6, 4]
k = 2

print(kthLargest(nums, len(nums), k))
