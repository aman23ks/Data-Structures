
class Solution:
    def f(self, node, parent, nums, dp):
        if node == len(nums):
            return 0
        
        if dp[node][parent+1] != -1:
            return dp[node][parent+1]
        
        l = self.f(node + 1, parent, nums, dp)
        
        if parent == -1 or nums[node] > nums[parent]:
            take = 1 + self.f(node + 1, node, nums, dp)
        else:
            take = 0
    
        l = max(take,l)
        
        dp[node][parent+1] = l
        
        return dp[node][parent+1]
    
    #Function to find length of longest increasing subsequence.
    def longestSubsequence(self,a,n):
        # code here
        dp = [[-1 for i in range(n+1)] for i in range(n+1)]
        return self.f(0, -1, a, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        ob=Solution()
        print(ob.longestSubsequence(a,n))
# } Driver Code Ends