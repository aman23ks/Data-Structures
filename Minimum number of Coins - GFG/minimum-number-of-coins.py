#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here
        curr = [1,2,5,10,20,50,100,200,500,2000]
        curr.sort(reverse = True)
        
        i = 0
        ans = []
        
        while i < len(curr):
            if curr[i] > N:
                i += 1
            else:
                ans.append(curr[i])
                N = N - curr[i]
        
        return ans
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends