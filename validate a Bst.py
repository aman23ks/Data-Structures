# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        self.arr = []
        self.inorder(root)

        for i in range(len(self.arr)-1):
            if self.arr[i] >= self.arr[i+1]:
                return False
        return True

    def inorder(self, root):
        if root == None:
            return
        self.inorder(root.left)
        self.arr.append(root.val)
        self.inorder(root.right)
