class Solution:
	def overlappedInterval(self, Intervals):
		#Code here
		    intervals = Intervals
		
            if intervals == []:
                return 
            
            intervals = sorted(intervals)
            
            result = []
            for interval in intervals:
                if result == [] or result[-1][1] < interval[0]:
                    result.append(interval)
                else:
                    result[-1][1] = max(interval[1], result[-1][1])
                
            return result

#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	n = int(input())
    	a = list(map(int, input().strip().split()))
    	Intervals = []
    	j = 0
    	for i in range(n):
    		x = a[j]
    		j += 1
    		y = a[j]
    		j += 1
    		Intervals.append([x,y])
    	obj = Solution()
    	ans = obj.overlappedInterval(Intervals)
    	for i in ans:
    		for j in i:
    			print(j, end = " ")
    	print()
# } Driver Code Ends