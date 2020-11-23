# Selection sort involves finding the minimum element in one pass through the array
# and then swapping it with the first position of the unsorted part of the array.
# Time complexity of selection sort is O(n^2) in all cases

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]


def SelectionSort(array):
    # -1 because when only 1 elment remians, it will be already be sorted
    for i in range(len(array)):
        # We set the minixmum element to be the ith element
        minimum = array[i]
        mimimum_index = i  # And the minimum index to be the ith index
        # Then we check the array from the i+1th element to the end
        for j in range(i+1, len(array)):
            # If a smaller element than the minimum element is found, we re-assign the minimum element and the minimu index
            if minimum > array[j]:
                mimimum_index = j
                minimum = array[j]
        if mimimum_index != i:  # If minimum index has changed, i.e, a smaller  element has been found, then we swap that element with the ith element
            array[mimimum_index], array[i] = array[i], array[mimimum_index]
    return array


print(SelectionSort(numbers))
