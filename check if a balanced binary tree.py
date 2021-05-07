def isBalanced(self, root):
    return self.doCheck(root) != float("inf")


def doCheck(self, root):
    if root == None:
        return 0

    left = self.doCheck(root.left) + 1
    right = self.doCheck(root.right) + 1

    if abs(left - right) > 1:
        return float("inf")
    else:
        return max(left, right)
