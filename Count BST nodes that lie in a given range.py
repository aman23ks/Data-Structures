def check(root, count, low, high):
    if not root:
        return

    if root.data >= low and root.data <= high:
        count[0] += 1

    check(root.left, count, low, high)
    check(root.right, count, low, high)


def getCount(root, low, high):
    # Your code here

    count = [0]
    check(root, count, low, high)
    return count[0]
