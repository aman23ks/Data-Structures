def isIsomorphic(self, root1, root2):

    if (not root1 and not root2):
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False

    a = self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(
        root1.right, root2.right)
    b = self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(
        root1.right, root2.left)

    return a or b
