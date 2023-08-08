#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
	    nums=arr
    	# code here
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == 0:
                if nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    j += 1
            else:
                i += 1
                j += 1
        return nums

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends