#User function Template for python3


class Solution:

    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
       
        # code here
        t = [[0 for x in range(W + 1)] for x in range(n + 1)]
        
        for i in range(n+1):
            for j in range(W+1):
                if i == 0  or j == 0:
                    t[i][j] = 0
                    
                elif (wt[i-1] <= j):
                    t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]], t[i-1][j])
                
                else:
                    t[i][j] = t[i-1][j]
                
        
        return t[n][W]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends