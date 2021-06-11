def func(root, ans):
    if not root:
        return 0
    l = func(root.left, ans)
    r = func(root.right, ans)
    if l+r+root.data > ans[0]:
        ans[0] = l+r+root.data
    return l+r+root.data


def largestSubtreeSum(root):
    # Write your code here.
    ans = []
    ans.append(float("-inf"))
    func(root, ans)
    return ans[0]
