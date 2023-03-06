#User function Template for python3

class Solution:
    def floor(self, root, x):
        # Code here
        floor = -1
        while root != None:
            if root.data > x:
                root = root.left
            elif root.data < x:
                floor = root.data
                root = root.right
            else:
                return root.data
        
        return floor

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def insert(tree, val):
    if(tree==None):
        return Node(val)
    if(val< tree.data):
        tree.left= insert(tree.left, val)
    elif(val > tree.data):
        tree.right= insert(tree.right, val)
    return tree
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        arr= list(map(int, input().split()))
        root = None
        for k in arr:
            root=insert(root, k)
        s=int(input())
        obj = Solution()
        print(obj.floor(root,s))
# } Driver Code Ends