arr = [[0, 1, 1, 1],
       [0, 0, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]

for row in arr:
    l = 0
    r = len(arr)
    count = 0
    while l < r:
        mid = (l+r)//2
        if row[mid] == 1:
            r = mid - 1
        else:
            l = mid + 1
    count += r
