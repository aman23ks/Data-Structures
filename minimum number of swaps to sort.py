# nums = [13, 1, 5, 3, 6, 11, 10]
# nums = [2, 8, 5, 4]
# nums = [10, 19, 6, 3, 5]
nums = [7, 16, 14, 17, 6, 9, 5, 3, 18]

values = []
count = 0

for i in range(len(nums)):
    values.append([nums[i], i])

values = sorted(values)

i = 0
while i < len(nums)-1:
    if values[i][1] == i:
        i += 1
        continue
    else:
        count += 1
        var = values[i][1]
        print(var)
        temp = values[i]
        values[i] = values[var]
        values[var] = temp


print(values)
print(count)
