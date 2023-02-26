#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, ratings):
        # Code here
        L2R = [1 for i in range(len(ratings))]
        
        R2L = [1 for i in range(len(ratings))]
        ratings2 = ratings[::-1] 
        total = 0

        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                L2R[i] = L2R[i-1]+1
            if ratings2[i] > ratings2[i-1]:
                R2L[i] = R2L[i-1]+1
        
        R2L = R2L[::-1]     
        
        for i in range(len(ratings)):
            total += max(L2R[i], R2L[i])

        return total

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends