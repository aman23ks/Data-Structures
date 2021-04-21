# arr = [[0, 1, 1, 1],
#        [0, 0, 1, 1],
#        [1, 1, 1, 1],
#        [0, 0, 0, 0]]

# # arr = [
# #     [0, 0],
# #     [1, 1]
# # ]

# # values = []

# # for row in arr:
# #     l = 0
# #     r = len(arr)
# #     while l < r:
# #         m = (l+r)//2
# #         if row[m] == 1:
# #             r = m
# #         else:
# #             l = m + 1
# #     count = len(arr) - r
# #     values.append(count)

# # max_value = max(values)

# # index = values.index(max_value)

# # print(index)

# Python3 program to find the row
# with maximum number of 1s

# Function to find the index
# of first index of 1 in a
# boolean array arr[]
def first(arr, low, high):
    if high >= low:

        mid = low + (high - low)//2

        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return first(arr, (mid + 1), high)
        else:
            return first(arr, low, (mid - 1))
    return -1


def rowWithMax1s(mat):
    R = len(mat)
    C = len(mat[0])
    max_row_index = -1
    max = -1
    for i in range(0, R):
        index = first(mat[i], 0, C - 1)
        print(index)
        if index != -1 and C - index > max:
            max = C - index
            max_row_index = i

    return max_row_index


mat = [[0, 0, 0, 0]]
print("Index of row with maximum 1s is",
      rowWithMax1s(mat))
