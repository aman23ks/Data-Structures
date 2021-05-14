def kthLargest(self, root, k):

    self.counter = 0
    self.k_largest = None

    def inorder(root):
        if root == None or self.k_largest:
            return

        inorder(root.right)

        self.counter += 1
        if self.counter == k:
            self.k_largest = root.data

        inorder(root.left)


inorder(root)
if self.k_largest:
    print(self.k_largest)
