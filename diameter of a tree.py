def diameterOfBinaryTree(self, root):
    self.ptr = 0

    def recursion(root):
        if root == None:
            return 0
        l = recursion(root.left)
        r = recursion(root.right)

        if l+r > self.ptr:
            self.ptr = l+r

        return 1 + max(l, r)

    recursion(root)
    return self.ptr
