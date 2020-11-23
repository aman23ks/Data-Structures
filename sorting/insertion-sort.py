# In Insertion sort, for the first iteration we fix the first element, assuming it is at its correct position
# Then we loop through the rest of the elements and insert them in their correct positions, with respect to the already sorted part of the array
# Time complexity is O(n^2) in worst case

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def InsertionSort(array):
    for i in range(1, len(array)):
        value = array[i]
        j = i - 1
        while j >= 0:
            if value < array[j]:
                array[j+1] = array[j]
                array[j] = value
                j = j-1
            else:
                break
    return array


print(InsertionSort(numbers))
