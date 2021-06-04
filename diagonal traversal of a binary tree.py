def diagonal(root):

    q = []
    ans = []
    if not root:
        return ans
    q.append(root)

    while q:
        temp = q.pop(0)
        # print(q)
        while temp:
            if temp.left:
                q.append(temp.left)
            ans.append(temp.data)
            temp = temp.right

    return ans
