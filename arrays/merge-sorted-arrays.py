# Merge sorted arrays
# Given two arrays [0,3,4,31] , [4,6,30]
# Output : [0,3,4,4,6,31]

# This method only works for numbers.
def mergeSortedArrays(array1, array2):
    # Even if any one array is empty for eg. array1 = [] then array3 = array2
    array3 = array1 + array2
    for i in range(0, len(array3)-1):  # loops through  array3
        # Checks the elements in array3 if predecessor is bigger than successor the it swaps them
        if array3[i] > array3[i+1]:
            # the predecessor is stored in a temporary variable
            temp = array3[i]
            # the successor is stored in the container of the predecessor
            array3[i] = array3[i+1]
            # the predecessor which was stored in the temporary variable is stored in the container of the successor
            array3[i+1] = temp
    return array3  # return array3


array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]
print(mergeSortedArrays(array1, array2))

# # This method works for strings as well as numbers
# def mergeSortedArrays(array1, array2):
#     array3 = array1 + array2  # Concatenate and store value in array3
#     array3.sort()  # Sort array3 , works for strings as well as integers
#     return array3  # return array3


# array1 = [0, 3, 4, 31]
# array2 = [4, 6, 30]

# print(mergeSortedArrays(array1, array2))
