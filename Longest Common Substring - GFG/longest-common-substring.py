#User function Template for python3

#User function Template for python3

class Solution:
    def lcs(self, s1, s2, n, m, res, dp):
        
        for i in range(n+1):
            dp[i][0] = 0
        
        for i in range(m+1):
            dp[0][i] = 0
            
        for i in range(1, n+1):
            for j in range(1, m+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
            
        ans = float("-inf")    
        for i in range(n+1):
            for j in range(m+1):
                ans = max(ans, dp[i][j])
        
        return ans
        
        # if n == 0 or m == 0:
        #     return res
            
        # if dp[n][m] != -1:
        #     return dp[n][m]
            
        # if s1[n-1] == s2[m-1]:
        #     dp[n][m] = self.lcs(s1, s2, n-1, m-1, res+1, dp)
             
        # else:
        #     dp[n][m] = max(res, max(self.lcs(s1, s2, n-1, m, 0, dp), self.lcs(s1, s2, n, m-1, 0, dp)))
        
        # return dp[n][m]
        
        
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        
        dp = [[-1 for i in range(m+1)]for i in range(n+1)]
        
        return self.lcs(S1, S2, n, m, 0, dp)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n,m = input().strip().split(" ")
        n,m = int(n), int(m)
        S1 = input().strip()
        S2 = input().strip()
        
        
        ob=Solution()
        print(ob.longestCommonSubstr(S1, S2, n, m))
# } Driver Code Ends