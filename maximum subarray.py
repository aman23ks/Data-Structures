def maxSubArray(self, nums):
    if len(nums) == 0:
        return 0

    sum_max = nums[0]
    sum_including_current = nums[0]
    for i in range(1, len(nums)):
        n = nums[i]
        sum_including_current = max(sum_including_current + n, n)
        sum_max = max(sum_max, sum_including_current)

    return sum_max
