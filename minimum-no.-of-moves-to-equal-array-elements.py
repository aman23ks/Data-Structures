nums = [1, 2, 3]

if len(nums) <= 1:
    print(0)
if len(nums) == 2:
    print(abs(nums[0]-nums[1]))
min_moves = 0
diff = 0
nums = sorted(nums, reverse=True)
for i in range(len(nums)-1):
    diff = nums[i] - nums[-1]
    min_moves += diff
print(abs(min_moves))
