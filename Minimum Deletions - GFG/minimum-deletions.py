#User function Template for python3
class Solution:
    def lcs(self,s, s2, m, n,dp):
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
        for i in range(1,m+1):
            for j in range(1, n+1):
                if s[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    def minimumNumberOfDeletions(self,S):
        # code here 
        S2 = S[::-1]
        
        dp = [[-1 for i in range(len(S2)+1)] for j in range(len(S)+1)]
       
        return len(S) - self.lcs(S,S2,len(S),len(S2),dp)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends