N = 6
S = [1, 3, 0, 5, 8, 5]
F = [2, 4, 6, 7, 9, 9]

# S = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]
# F = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]
# N = 8


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
        value.append([start[i], end[i], i+1])
    value = sort_array(value, n)
    print(value)
    i = 0
    j = 1
    ans = []

    while j < n:
        print(value[i][1], value[j][0])
        if value[i][1] < value[j][0]:
            print(value[i][2])
            ans.append(value[i][2])
            i = j
            j += 1
        else:
            j += 1

    ans.append(value[-1][2])
    return ans


print(maximumMeetings(N, S, F))

# Python3 program to find maximum number
# of meetings

# Custom class for storing starting time,
# finishing time and position of meeting.
# class meeting:

#     def __init__(self, start, end, pos):

#         self.start = start
#         self.end = end
#         self.pos = pos

# # Function for finding maximum
# # meeting in one room


# def maxMeeting(l, n):

#     # Initialising an arraylist
#     # for storing answer
#     ans = []

#     # Sorting of meeting according to
#     # their finish time.
#     l.sort(key=lambda x: x.end)
#     for i in range(n):
#         print(l[i].start, l[i].end, l[i].pos)
#     # Initially select first meeting
#     ans.append(l[0].pos)

#     # time_limit to check whether new
#     # meeting can be conducted or not.
#     time_limit = l[0].end

#     # Check for all meeting whether it
#     # can be selected or not.
#     for i in range(1, n):
#         if l[i].start > time_limit:
#             ans.append(l[i].pos)
#             time_limit = l[i].end

#     # Print final selected meetings
#     for i in ans:
#         print(i + 1, end=" ")

#     print()


#     # Driver code
# if __name__ == '__main__':

#     # Starting time
#     s = [75250, 50074, 43659, 8931, 11273, 27545, 50879, 77924]

#     # Finish time
#     f = [112960, 114515, 81825, 93424, 54316, 35533, 73383, 160252]

#     # Number of meetings.
#     n = len(s)

#     l = []

#     for i in range(n):

#         # Creating object of meeting
#         # and adding in the list
#         l.append(meeting(s[i], f[i], i))

#     # Function call
#     maxMeeting(l, n)
