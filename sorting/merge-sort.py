# Merge Sort uses the Divide and Conquer approach. It involves breaking up the array from the middle until
# Arrays of only 1 elements remain and thein merging them back up in a sorted order.
# Time complexity is O(nlog N) and space complexity is O(n)

array = [5, 9, 3, 10, 44, 2, 0]


def Merge_sort(array):
    if len(array) == 1:
        return array
    else:
        length = len(array)
        middle = length // 2
        left = array[:middle]
        right = array[middle:]
        print("left: " + str(left))
        print("right: " + str(right))
        return merge(Merge_sort(left), Merge_sort(right))


def merge(left, right):
    left_index = 0
    right_index = 0
    length_left = len(left)
    length_right = len(right)
    sorted_array = []
    while left_index < length_left and right_index < length_right:
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1

    print("merge left: " + str(left))
    print("merge right: " + str(right))
    print("sorted array: " + str(sorted_array))
    return sorted_array + left[left_index:]+right[right_index:]


print(Merge_sort(array))
