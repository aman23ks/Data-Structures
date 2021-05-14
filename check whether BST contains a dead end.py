def isdeadEnd(root):
    # Code here

    def isDeadEnd(root, min, max):
        if root == None:
            return False

        if (max-min) <= 2:
            return True

        return isDeadEnd(root.left, min, root.data) or isDeadEnd(root.right, root.data, max)

    return isDeadEnd(root, 0, float("inf"))
