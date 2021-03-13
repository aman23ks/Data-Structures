# Definition for a binary tree node.
# Recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode):
        s = []

        def preorder(root):
            if root == None:
                return
            s.append(root.val)
            preorder(root.left)
            preorder(root.right)

        preorder(root)
        return s

# Iterative


class Solution2:
    def preorderTraversal(self, root: TreeNode):
        stack = []
        traversal = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                traversal.append(node.val)
                node = node.left
            else:
                node = stack.pop()
                node = node.right
        return traversal
