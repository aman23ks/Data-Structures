# If in this question you don't need to change the array then create a new array and make changes in that.
count = 0


def mergeSort(arr):
    if len(arr) == 1:
        return arr
    left = arr[0:len(arr)//2]
    right = arr[len(arr)//2:]

    return Merge(mergeSort(left), mergeSort(right))


def Merge(left, right):
    global count
    left_index = 0
    right_index = 0
    left_length = len(left)
    right_length = len(right)
    sorted_array = []
    while left_index < left_length and right_index < right_length:
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        elif left[left_index] > right[right_index]:
            sorted_array.append(right[right_index])
            right_index += 1
            count += left_length - left_index
        else:
            left_index += 1
            right_index += 1
            # If you have all the elements same as for eg. [10,10,10] you don't need to maintain a sorted array because the answer will always be zero so no need to maintain it just increment the counter.
    return sorted_array + left[left_index:] + right[right_index:]


def inversionCount(arr):
    # Your Code Here
    global count
    mergeSort(arr)
    return count


print(inversionCount([5, 3, 2, 4, 1]))
