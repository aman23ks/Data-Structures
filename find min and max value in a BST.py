
class Node:
    data = 0
    left = None
    right = None


def minValue(root):
    # Your code here
    if root.left == None and root.right == None:
        return root.data
    while root.left:
        root = root.left
    return root.data


def maxValue(root):
    # Your code here
    if root.left == None and root.right == None:
        return root.data
    while root.right:
        root = root.right
    return root.data
