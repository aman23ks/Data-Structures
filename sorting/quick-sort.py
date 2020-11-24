# Quick Sort is another sorting algorithm which follows divide and conquer approach.
# It requires to chose a pivot, then place all elements smaller than the pivot on the left of the pivot and all elements larger on the right
# Then the array is partitioned in the pivot position and the left and right arrays followthe same procedure until the base case is reached.
# After each pass the pivot element occupies its correct position in the array.
# Time Complexity in Best and Average cases is O(nlog N) whereas in worst case it jumps up to O(n^2). Space complexity is O(log n)

# In this implementation, we will take the last element as pivot.

from random import randint

array = [6, 7, 3, 1, 8, 7, 2, 4]


def QuickSort(array):
    if len(array) <= 1:
        return array
    else:
        smaller, equal, larger = [], [], []
        # Using a randomized pivot we can avoid hitting the ever worst case time complexity by avoiding picking our pivot from the same location in every recursive call.
        pivot = array[randint(0, len(array)-1)]
        for element in array:
            if element > pivot:
                larger.append(element)
            elif element == pivot:
                equal.append(element)
            elif element < pivot:
                smaller.append(element)
        return QuickSort(smaller) + equal + QuickSort(larger)


print(QuickSort(array))
