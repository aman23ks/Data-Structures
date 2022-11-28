#User function Template for python3


class Solution:
    def fill(self, n, m, mat):
        # code here
        board = mat
        boundary = []

        visited = [[0 for i in range(len(board[0]))] for i in range(len(board))]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or i == len(board) - 1 or j == 0 or j == len(board[0]) - 1:
                    if board[i][j] == "O":
                        boundary.append([i, j])

        # print(boundary)

        while boundary:
            x, y = boundary.pop(0)

            visited[x][y] = 1

            lst = [[x + 1, y], [x - 1, y], [x, y - 1], [x, y + 1]]

            for i, j in lst:
                if 0 <= i <= len(board) - 1 and 0 <= j <= len(board[0]) - 1:
                    if board[i][j] == "O" and visited[i][j] == 0:
                        visited[i][j] = 1
                        boundary.append([i, j])

        for i in range(len(board)):
            for j in range(len(board[0])):
                if visited[i][j] == 0:
                    board[i][j] = "X"
                elif visited[i][j] == 1:
                    board[i][j] = "O"
                    
        return board

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends