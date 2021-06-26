# N = 6
# S = [1, 3, 0, 5, 8, 5]
# F = [2, 4, 6, 7, 9, 9]

N = 8
S = [75250, 50074, 43659, 8931, 11273,
     27545, 50879, 77924]
F = [112960, 114515, 81825, 93424, 54316,
     35533, 73383, 160252]


def sort_array(value, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if value[i][1] > value[j][1]:
                temp = value[i]
                value[i] = value[j]
                value[j] = temp
            elif value[i][1] == value[j][1]:
                if value[i][0] > value[j][0]:
                    temp = value[i]
                    value[i] = value[j]
                    value[j] = temp
    return value


def maximumMeetings(n, start, end):
    value = []
    for i in range(n):
        value.append([start[i], end[i]])
    value = sort_array(value, n)
    i = 0
    j = 1
    c = 1

    while j < n:
        if value[i][1] < value[j][0]:
            c += 1
            i = j
            j += 1
        else:
            j += 1

    return c


print(maximumMeetings(N, S, F))
