#User function Template for python3


class Solution:
    def count(self, text1, text2, n, m, dp):
        if m == 0 or n == 0:
            return 0
        
        if dp[n][m] != -1:
            return dp[n][m]
        
        if text1[n-1] == text2[m-1]:
            dp[n][m] = 1 + self.count(text1, text2, n-1, m-1, dp)
        else:
            dp[n][m] = max(self.count(text1, text2, n-1, m, dp),self.count(text1, text2, n, m-1, dp))
        
        return dp[n][m]
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        dp = [[-1 for i in range(n+1)] for i in range(m+1)]
        return len(X+Y) - self.count(X,Y,m,n, dp)
         #code here

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__': 
    t=int(input())
    for tcs in range(t):
        X,Y=input().split()
        
        print(Solution().shortestCommonSupersequence(X,Y,len(X),len(Y)))
        
# } Driver Code Ends