def search(root, key):
    if root is None or root == key:
        return root
    elif root.data < key:
        search(root.right, key)
    elif root.data > key:
        search(root.left, key)
