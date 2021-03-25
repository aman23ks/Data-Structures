import math


class Solution:
    def countSquares(self, N):
        # code here
        a = int(math.sqrt(N))
        if a*a == N:
            return a-1
        else:
            return a
