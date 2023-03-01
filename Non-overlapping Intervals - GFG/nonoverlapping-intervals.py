#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, N, intervals):
        # Code here
        intervals = sorted(intervals)
        l = 0
        r = 1
        count = 0
        while r<len(intervals):
            if intervals[l][1] <= intervals[r][0]: #Case 1
                l = r
                r += 1
            elif intervals[l][1] <= intervals[r][1]: #Case 2
                r += 1
                count += 1
            elif intervals[l][1] > intervals[r][1]:
                l = r
                r += 1
                count += 1
        
        return count

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(N, intervals)
        print(res)
# } Driver Code Ends