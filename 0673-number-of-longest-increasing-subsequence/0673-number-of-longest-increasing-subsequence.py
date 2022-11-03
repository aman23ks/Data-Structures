class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        maxi = float("-inf")
        dp = [1 for i in range(len(nums))]
        count = [1 for i in range(len(nums))] 
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j] and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]  
                    count[i] = count[j]
                elif nums[i]>nums[j] and dp[i] == 1 + dp[j]:
                    count[i] += count[j]
        
            maxi = max(maxi, dp[i])
        print(dp)
        print(count)
        print(maxi)
        nos = 0
        for i in range(len(nums)):
            if dp[i] == maxi:
                nos += count[i]
        
        return nos