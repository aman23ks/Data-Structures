from typing import List


class Solution:
    def solve(self,nums,i,j,dp):
        if i>j:
            return 0
        
        if dp[i][j] != -1:
            return -1

        mx = float("-inf")

        for k in range(i,j+1):
            if dp[i][k-1] != -1:
                left = dp[i][k-1]
            else:
                left = self.solve(nums, i, k-1,dp)
            
            if dp[k+1][j] != -1:
                right = dp[k+1][j]
            else:
                right = self.solve(nums, k+1, j,dp)
            
            temp = left + right + (nums[i-1]*nums[k]*nums[j+1])
            mx = max(temp,mx)
        
        dp[i][j] = mx

        return dp[i][j]
        
    def maxCoins(self, N : int, arr : List[int]) -> int:
        # code here
        arr = [1] + arr + [1]
        
        dp = [[-1 for i in range(len(arr)+1)]for i in range(len(arr)+1)]
        
        return self.solve( arr, 1, len(arr)-2, dp)



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        arr=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxCoins(N, arr)
        
        print(res)
        

# } Driver Code Ends