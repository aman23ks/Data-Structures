def toSumTree(self, root):
    # code here
    return self.check(root)


def check(self, root):
    if root == None:
        return 0

    left = self.check(root.left)
    right = self.check(root.right)

    curr_node = root.data
    ans = left+right
    root.data = ans
    return curr_node + ans
