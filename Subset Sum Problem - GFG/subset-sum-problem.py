#User function Template for python3

class Solution:
    # dp = [[-1 for i in range(100001)] for i in range(101)]
    def isSubsetSum (self, N, arr, sum):
        # code here 
        
        dp = [[-1 for i in range(sum+1)] for i in range(N+1)]
        
        for i in range(N+1):
            for j in range(sum+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                
                if i != 0 and j == 0:
                    dp[i][j] = 1
                
                if i == 0 and j != 0:
                    dp[i][j] = 0
                    
                
        for i in range(1,N+1):
            for j in range(1,sum+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                elif arr[i-1] > j:
                    dp[i][j] = dp[i-1][j]
        
        return dp[N][sum]
                
        # if sum == 0 and N == 0:
        #     self.dp[N][sum] = 1
        
        # if sum == 0 and N != 0:
        #     self.dp[N][sum] = 1
        
        # if sum != 0 and N==0:
        #     self.dp[N][sum] = 0
        
        # if self.dp[N][sum] != -1:
        #     return self.dp[N][sum]
            
        # if arr[N-1] <= sum:
        #     self.dp[N][sum] = self.isSubsetSum(N-1, arr, sum - arr[N-1]) or (self.isSubsetSum(N-1, arr, sum))
        # elif arr[N-1] > sum:
        #     self.dp[N][sum] = self.isSubsetSum(N-1, arr, sum)
        
        # return self.dp[N][sum]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(N,arr,sum)==True:
            print(1)
        else :
            print(0)
            
        

# } Driver Code Ends