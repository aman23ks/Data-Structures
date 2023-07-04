
class Solution:
    def trappingWater(self, arr,n):
        height = arr
        #Code here
        l = []
        
        r = []
        
        l_max = 0
        
        r_max = 0
        
        for i in range(len(height)):
            if height[i] <= l_max:
                l.append(l_max)
            elif height[i] > l_max:
                l_max = height[i]
                l.append(l_max)

        for i in range(len(height)-1,-1,-1):
            if height[i] <= r_max:
                r.append(r_max)
            elif height[i] > r_max:
                r_max = height[i]
                r.append(r_max)

        r = r[::-1]
        res = 0
        for i in range(len(height)):
            res += min(l[i],r[i]) - height[i]
        
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math



def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            obj = Solution()
            print(obj.trappingWater(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()



# } Driver Code Ends