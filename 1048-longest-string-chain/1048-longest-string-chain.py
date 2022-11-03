class Solution:
    def compare(self, A, B):
        if len(A) != len(B)+1:
            return False
        
        i = 0
        j = 0
        
        while i<len(A):
            
            if j < len(B) and A[i] == B[j]:
                i += 1
                j += 1
            else:
                i += 1
         
        if i == len(A) and j == len(B):
            return True
        return False
        
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key = lambda x: len(x))
        dp = [1 for i in range(len(words))]
        
        maxi = float("-inf")
        
        for i in range(len(words)):
            for j in range(i):
                if self.compare(words[i], words[j]) and dp[i] < 1 + dp[j]:
                    dp[i] = 1 + dp[j]
            
            maxi = max(dp[i], maxi)
            
        return maxi