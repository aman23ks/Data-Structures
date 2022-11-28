#User function Template for python3
#User function Template for python3

import sys

class Solution:
   
    def travel(self, idx, visited, cost, dp, v):
        if visited>v:
            return 0
        
        if v == visited:
            return cost[idx][0]
        
        ans = float("inf")
        
        for i in range(1,v):
            if idx != i and dp[i] == -1:
                dp[i] = 1
                visited += 1
                ans = min(ans, cost[idx][i] + self.travel(i,visited,cost,dp,v))
                dp[i] = -1
                visited -= 1
                
        return ans
                
    
    
    def total_cost(self, cost):
        if len(cost) == 1:
            return cost[0][0]
            
        dp = [-1 for i in range(len(cost)+1)]
        
        return self.travel(0,1,cost,dp,len(cost))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		cost = []
		for _ in range(n):
			cost.append(list(map(int, input().split())))
		obj = Solution()
		ans = obj.total_cost(cost)
		print(ans)

# } Driver Code Ends