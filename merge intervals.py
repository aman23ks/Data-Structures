def merge(intervals):
    if intervals == []:
        return

    intervals = sorted(intervals)

    result = []
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(interval[1], result[-1][1])

    return result


print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
