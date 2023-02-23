#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        # code here
        
        arr.sort()
        dep.sort()
        
        plt = 1
        
        mx = 1
        
        i = 0
        j = 1
        
        while j < len(arr):
            if dep[i] >= arr[j]:
                plt += 1
                mx = max(mx, plt)
                j += 1
            else:
                i += 1
                plt -= 1
        
        return mx
                 
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob=Solution()
        print(ob.minimumPlatform(n,arrival,departure))
# } Driver Code Ends