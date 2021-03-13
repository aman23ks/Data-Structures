# Definition for a binary tree node.
# Recursion
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        s = []

        def preorder(root):
            if root == None:
                return
            preorder(root.left)
            s.append(root.val)
            preorder(root.right)

        preorder(root)
        return s

# Iterative


class Solution2:
    def inorderTraversal(self, root: TreeNode):
        traversal = []
        stack = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                traversal.append(node.val)
                node = node.right
        return traversal
