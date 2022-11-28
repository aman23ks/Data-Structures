class Solution:

    #Function to find minimum time required to rot all oranges. 
    def orangesRotting(self, grid):
            row = len(grid)
            column = len(grid[0])
            fresh = 0
            t = 0
            rotten = []
            for i in range(row):
                for j in range(column):
                    if grid[i][j] == 2:
                        rotten.append([i, j])
                    elif grid[i][j] == 1:
                        fresh += 1
    
            while len(rotten) > 0:
                for i in range(len(rotten)):
                    x, y = rotten[0]
                    rotten.pop(0)
                    lst = [[x-1, y], [x, y-1], [x+1, y], [x, y+1]]
                    for r, c in lst:
                        if r >= 0 and c >= 0 and r < row and c < column and grid[r][c] == 1:
                   
                            grid[r][c] = 2
                            fresh -= 1
                            rotten.append([r, c])
                            
                if len(rotten) > 0:
                    t += 1
    
            if fresh == 0:
                return t
            else:
                return -1

#{ 
 # Driver Code Starts
from queue import Queue

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = map(int, input().split())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.orangesRotting(grid)
		print(ans)

# } Driver Code Ends