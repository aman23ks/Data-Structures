nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

numbers = dict()
intersected_values = []
for i in nums1:
    if i in numbers:
        numbers[i] += 1
    else:
        numbers[i] = 1

for i in nums2:
    if i in numbers:
        if i in intersected_values:
            continue
        else:
            intersected_values.append(i)

print(intersected_values)


# solutiion 2
#  return (set(nums1) & set(nums2))
