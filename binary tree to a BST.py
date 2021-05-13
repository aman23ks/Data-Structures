def binaryTreeToBST(self, root):
    # code here
    global index

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        value.append(root.data)
        inorder(root.right)

    def inorder2(root):
        global index
        if root == None:
            return
        inorder2(root.left)
        root.data = value[index]
        index += 1
        inorder2(root.right)

    value = []
    inorder(root)
    index = 0
    value = sorted(value)
    inorder2(root)

    return root
