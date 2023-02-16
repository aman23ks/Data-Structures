#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def lemonadeChange(self, N, bills):
        # Code here
        fives=tens=0
        for i in bills:
            if i == 5:
                fives += 1
            elif i == 10 and fives:
                fives -= 1
                tens += 1
            elif i == 20 and tens and fives:
                tens-=1
                fives-=1
            elif i == 20 and fives >=3:
                fives -= 3
            else:
                return False
        return True

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        bills = list(map(int, input().split()))
        ob = Solution()
        res = ob.lemonadeChange(N, bills)
        print(res)
# } Driver Code Ends