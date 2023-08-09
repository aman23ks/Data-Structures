#User function Template for python3


class Solution:
    def missingNumber(self,array,n):
        nums = array
        s = ((len(nums)+1)*(len(nums)+2))//2
        s_a = 0
        for i in range(len(nums)):
            s_a += nums[i]
        return s-s_a
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().missingNumber(a,n)
    print(s)
# } Driver Code Ends