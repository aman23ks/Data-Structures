intervals = [[1, 4], [3, 6], [2, 8]]

arr = []

for i in range(len(intervals)):
    for j in range(len(intervals)):
        if i == j:
            continue
        if intervals[i][0] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
            if intervals[i] not in arr:
                arr.append(intervals[i])
        if intervals[i][0] <= intervals[j][0] and intervals[i][1] >= intervals[j][1]:
            if intervals[j] not in arr:
                arr.append(intervals[j])


final = len(intervals) - len(arr)
print(final)
