#User function template for Python

class Solution:	
	def remove_duplicate(self, A, N):
		# code here
		arr = A
		n = N
		i = 0
        j = 1
        while j < n:
            if arr[i] != arr[j]:
                i += 1
                arr[i] = arr[j]
                j += 1
    
            elif arr[i] == arr[j]:
                j += 1
    
        return i+1 


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        N = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        n = ob.remove_duplicate(A,N)
        for i in range(n):
            print(A[i], end=" ")
        print()


# } Driver Code Ends