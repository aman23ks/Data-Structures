def sumOfLongRootToLeafPath(root):
    # code here
    def check(root):
        if not root:
            return [0, 0]

        left = check(root.left)
        right = check(root.right)

        if left[0] > right[0]:
            return [left[0]+1, left[1]+root.data]
        if left[0] < right[0]:
            return [right[0]+1, right[1]+root.data]
        else:
            return [left[0]+1, max(left[1], right[1]) + root.data]

    ans = check(root)
    return ans[1]
