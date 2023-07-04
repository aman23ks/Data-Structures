#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
	    l = None
	    sl = None
	    
	    for i in arr:
	       # print(l,sl)
	        if l == None and sl == None:
	            l = i
	        elif sl == None:
    	            if i > l:
    	                sl = l
    	                l = i
    	            elif i<l:
    	                sl = i
	        elif sl!=None and l!=None:
	           # print(i,sl , i,l)
	            if i>l:
	                sl = l
	                l = i
	            elif i>sl and i<l:
	               # print(i,sl , i,l)
	                sl = i
	            
	    if sl == None: 
	        return -1
	    else:
	        return sl
		# code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends