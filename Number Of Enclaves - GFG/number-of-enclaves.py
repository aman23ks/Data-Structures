#User function Template for python3


from typing import List

class Solution:    
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        boundary = []
        
        board = grid
        
        visited = [[0 for i in range(len(board[0]))] for i in range(len(board))]
        
        count = 0
        
        c = 0
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 1:
                    c += 1       
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == 1:
                        boundary.append([i, j])


        while boundary:
            x, y = boundary.pop(0)

            visited[x][y] = 1

            lst = [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]

            for i, j in lst:
                if 0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1:
                 
                    if board[i][j] == 1 and visited[i][j] == 0:
                        visited[i][j] = 1
                        boundary.append([i, j])
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] == 1:
                    count += 1
                    
        return c - count

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
# } Driver Code Ends