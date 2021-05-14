def kthSmallest(self, root, k):
    self.counter = 0
    self.k_smallest = None

    def inorder(root):
        if root == None or self.k_smallest:
            return

        inorder(root.left)

        self.counter += 1
        if self.counter == k:
            self.k_smallest = root.val

        inorder(root.right)

    inorder(root)
    return self.k_smallest
