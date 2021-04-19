matrix = [[1, 5, 9],
          [10, 11, 13],
          [12, 13, 15]]
k = 8
n = len(matrix)
# print(len(matrix))
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
# l        m        r


def countLessEqual(val):
    count = 0
    for row in matrix:
        left = 0
        right = n
        while left < right:
            mid = (left+right)//2

            if row[mid] <= val:
                left = mid + 1
                print(left)
                print(mid)
                print(right)

                # print(val, left)
            else:
                right = mid
        count += left
        # print(val, count)
    return count


left = matrix[0][0]
right = matrix[-1][-1]
while left < right:
    mid = (left + right)//2
    if countLessEqual(mid) < k:
        left = mid + 1
        # print(left)
    else:
        right = mid

print(left)
