class Solution:
    def lcs(self,s1, s2, m, n, dp):
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                    
        for i in range(1,m+1):
            for j in range(1,n+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                    
        return dp[m][n]
    
    def minOperations(self, s1, s2):
        # code here
        dp = [[-1 for i in range(len(s2)+1)] for i in range(len(s1)+1)]
        
        lcs = self.lcs(s1,s2,len(s1),len(s2),dp)
        
        deletions = len(s1) - lcs
        insertions = len(s2) - lcs
        
        return deletions+insertions


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s1,s2 = input().split()
		ob = Solution()
		ans = ob.minOperations(s1,s2)
		print(ans)
# } Driver Code Ends