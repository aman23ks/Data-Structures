def printBoundaryView(root):

    def leftTree(root, ans):
        if not root:
            return

        if root.left:
            ans.append(root.data)
            leftTree(root.left, ans)
        elif root.right:
            ans.append(root.data)
            leftTree(root.right, ans)

    def leavesTree(root, ans):
        if not root:
            return
        leavesTree(root.left, ans)
        if not root.left and not root.right:
            ans.append(root.data)
        leavesTree(root.right, ans)

    def rightTree(root, ans):
        if not root:
            return
        if root.right:
            rightTree(root.right, ans)
            ans.append(root.data)
        elif root.left:
            rightTree(root.left, ans)
            ans.append(root.data)

    ans = []
    ans.append(root.data)
    leftTree(root.left, ans)
    leavesTree(root, ans)
    rightTree(root.right, ans)

    return ans
