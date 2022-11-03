class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        hash_arr = [i for i in range(len(nums))]
        dp = [1 for i in range(len(nums))]
        maxi = float("-inf")
        last_index = 0
        # print(hash_arr)
        for i in range(len(nums)):
            for j in range(i):
                if (1 + dp[j] > dp[i]) and (nums[i] % nums[j] == 0):
                    dp[i] = 1 + dp[j]
                    hash_arr[i] = j
            
            if dp[i] > maxi:
                maxi = dp[i]
                last_index = i
            
        temp = [nums[last_index]]
        # print(dp)
        # print(hash_arr)
        while hash_arr[last_index] != last_index:
            last_index = hash_arr[last_index]
            temp.append(nums[last_index])
        # temp.append(nums[last_index])
        return temp[::-1]