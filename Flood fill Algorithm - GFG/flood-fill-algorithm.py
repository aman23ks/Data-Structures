class Solution:
    def dfs(self, image, sr, sc, color, value):

        image[sr][sc] = color

        dir = [[sr - 1, sc], [sr + 1, sc], [sr, sc - 1], [sr, sc + 1]]

        for i, j in dir:
            if -1 < i < len(image) and -1 < j < len(image[0]) and image[i][j] == value:
                self.dfs(image, i, j, color, value)

        return image
        
    def floodFill(self, image, sr, sc, newColor):
        #Code here
        if newColor == image[sr][sc]:
            return image
        
        return self.dfs(image, sr, sc, newColor, image[sr][sc])



#{ 
 # Driver Code Starts
import sys
sys.setrecursionlimit(10**7)
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n)
		m = int(m)
		image = []
		for _ in range(n):
			image.append(list(map(int, input().split())))
		sr, sc, newColor = input().split()
		sr = int(sr); sc = int(sc); newColor = int(newColor);
		obj = Solution()
		ans = obj.floodFill(image, sr, sc, newColor)
		for _ in ans:
			for __ in _:
				print(__, end = " ")
			print()
# } Driver Code Ends