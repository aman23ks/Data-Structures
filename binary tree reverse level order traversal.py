def levelOrderBottom(self, root):
    if not root or root.val == None:
        return

    q = [root]
    values = []

    while q:
        level_values = []
        for i in range(len(q)):
            node = q.pop(0)

            level_values.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        values.insert(0, level_values)
    return values
