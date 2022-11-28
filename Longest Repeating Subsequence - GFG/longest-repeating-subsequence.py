#User function Template for python3
#User function Template for python3

class Solution:
    def lcs(self,s1,s2,m,n,dp):
        for i in range(len(s1)+1):
            for j in range(len(s2)+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
        for i in range(1,m+1):
            for j in range(1,n+1):
                if (s1[i-1] == s2[j-1]) and i != j:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        
        return dp[m][n]
    
    def LongestRepeatingSubsequence(self, str):
        # Code here 
        
        dp = [[-1 for i in range(len(str)+ 1)] for i in range(len(str)+1)]
        
        return self.lcs(str,str,len(str),len(str),dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		str = input()
		ob = Solution()
		ans = ob.LongestRepeatingSubsequence(str)
		print(ans)

# } Driver Code Ends