# nums = [13, 1, 5, 3, 6, 11, 10]
# nums = [2, 8, 5, 4]
# nums = [10, 19, 6, 3, 5]
nums = [7, 16, 14, 17, 6, 9, 5, 3, 18]

values = []
count = 0


# def check(i, values):
#     global count
#     count += 1
#     var = values[i][1]
#     temp = values[i]
#     values[i] = values[var]
#     values[var] = temp

#     if values[i][1] != i:
#         check(i, values)


for i in range(len(nums)):
    values.append([nums[i], i])
# print(values[0][1])
print(values)
values = sorted(values)
# print(values)
# for i in range(len(values)-1):
#     # print(values[[i][1]])
#     if values[i][1] == i:
#         # print(values[i])
#         continue
#     else:
#         check(i, values)

i = 0
while i < len(nums)-1:
    if values[i][1] == i:
        # print(values[i])
        continue
    else:
        count += 1
        var = values[i][1]
        temp = values[i]
        values[i] = values[var]
        values[var] = temp

        i += 1


print(values)
# print(values)
print(count)
