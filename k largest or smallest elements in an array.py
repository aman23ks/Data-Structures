arr = [1, 23, 12, 9, 30, 2, 50]
size = len(arr)

# Size of Min Heap
k = 3


def FirstKelements(arr, size, k):
    min_heap = []
    for i in range(k):
        min_heap.append(arr[i])

    for i in range(k, size):

        # min_heap.sort(reverse=True)  For smallest elements
        min_heap.sort()

        # if min_heap[0] < arr[i]: #  For smallest elements
        if min_heap[0] > arr[i]:
            continue
        else:
            min_heap.pop(0)
            min_heap.append(arr[i])

    return min_heap


print(FirstKelements(arr, size, k))
