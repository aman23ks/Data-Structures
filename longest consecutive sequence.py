nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

nums = set(nums)
print(nums)
longest = 0

for n in nums:
    if (n-1) not in nums:
        length = 0
        while n + length in nums:
            length += 1

    longest = max(longest, length)

print(longest)
