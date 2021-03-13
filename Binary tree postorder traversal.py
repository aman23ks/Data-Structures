# Definition for a binary tree node.
# Recursive
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode):
        s = []

        def postorder(root):
            if root == None:
                return
            postorder(root.left)
            postorder(root.right)
            s.append(root.val)

        postorder(root)
        return s

# Iterative


class Solution2:
    def postorderTraversal(self, root: TreeNode):
        traversal = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                traversal.append(node.val)
        return reversed(traversal)
