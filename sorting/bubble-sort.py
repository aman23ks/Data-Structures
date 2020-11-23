# In Bubble Sort, the largest value is bubbled up in every pass.
# Every two adjacent items are compared and they are swapped if they are in the wrong order.
# This way, after every pass, the largest element reaches to the end of the array.
# Time complexity of Bubble Sort in Worst and Average Case is O(n^2) and in best case, its O(n)
array = [6, 7, 3, 1, 8, 7, 2, 4]


def BubbleSort(array):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    return array


print(BubbleSort(array))
