'''
A Simple Approach is to traverse the given array one by one and compare every element with the given element ‘x’. If matches, then return index.
The above solution can be Optimized using the fact that the difference between all adjacent elements is at most k.
The idea is to start comparing from the leftmost element and find the difference between the current array element and x.
Let this difference be ‘diff’. From the given property of the array, we always know that x must be at least ‘diff/k’ away, so instead of searching one by one, 
we jump ‘diff/k’. 
'''


# x is the element to be searched in arr[0..n-1]
# such that all elements differ by at-most k.
def search(arr, n, x, k):

    # Traverse the given array starting from
    # leftmost element
    i = 0
    while (i < n):

        # If x is found at index i
        if (arr[i] == x):
            return i

        # Jump the difference between current
        # array element and x divided by k
        # We use max here to make sure that i
        # moves at-least one step ahead.
        i = i + max(1, int(abs(arr[i] - x) / k))

    print("number is not present!")
    return -1


# Driver program to test above function
arr = [2, 4, 5, 7, 7, 6]
x = 6
k = 2
n = len(arr)
print("Element", x, "is present at index", search(arr, n, x, k))
