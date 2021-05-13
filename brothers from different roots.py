def countPairs(root1, root2, x):

    count = 0
    arr2 = []
    arr1 = []

    def inorder(root):
        if root == None:
            return
        inorder(root.left)
        arr1.append(root.data)
        inorder(root.right)

    def inorder2(root):
        if root == None:
            return
        inorder2(root.left)
        arr2.append(root.data)
        inorder2(root.right)

    inorder(root1)
    inorder2(root2)

    i = 0
    j = len(arr2)-1

    while i < len(arr1) and j >= 0:
        if (arr1[i] + arr2[j]) == x:
            count += 1
            j -= 1
        elif (arr1[i] + arr2[j]) < x:
            i += 1
        else:
            j -= 1

    return count
