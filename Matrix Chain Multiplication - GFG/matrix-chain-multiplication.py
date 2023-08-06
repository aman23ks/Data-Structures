#User function Template for python3

class Solution:
    def solve(self, i,j,arr,dp):
        
        # for m in range(len(arr)+1):
        #     for n in range(len(arr)+1):
        #         if m == 0 or n == 0:
        #             dp[m][n] =0
        if i>=j:
            return 0
            
        if dp[i][j] != -1:
            return dp[i][j]
        
        mn = float("inf")
        
        for k in range(i,j):
            temp = self.solve(i,k,arr,dp) + self.solve(k+1,j,arr,dp) + arr[i-1]*arr[k]*arr[j]
        
            mn = min(temp,mn)
        
        dp[i][j] = mn
        
        return mn
        
    def matrixMultiplication(self, N, arr):
        dp = [[-1 for i in range(N+1)] for j in range(N+1)]
        # code here
        return self.solve(1,N-1,arr, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        print(ob.matrixMultiplication(N, arr))
# } Driver Code Ends