def rightSideView(self, root):
    if not root or root.val == None:
        return
    values = []
    q = [root]

    while q:
        level_values = []
        for _ in range(len(q)):
            node = q.pop(0)
            level_values.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        values.append(level_values)

    result = []
    for i in range(len(values)):
        result.append(values[i][-1])

    return result
