class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        #Your code here
        res = -1
        
        l = 0 
        r = N-1
        mid = (l+r)//2
        
        while l<=r:
            if A[mid] < X:
                l = mid + 1
                mid = (l+r)//2
            elif A[mid] > X:
                r = mid - 1
                mid = (l+r)//2
            else:
                if A[mid] == X:
                    res = mid
                    break
                
        res = mid
        
        return mid
                
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            NX=[int(x) for x in input().strip().split()]
            N=NX[0]
            X=NX[1]

            A=[int(x) for x in input().strip().split()]
            
            obj = Solution()
            print(obj.findFloor(A,N,X))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends