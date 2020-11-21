# # Binary Search Trees are a non-linear data structure.
# # They consist of a root node and zero, one or two children where the children can again have 0,1, or 2 nodes as their children and so on
# # In most cases, the time complexity of operations on a BST, which include, lookups, insertions and deletions, take O(log N) time
# # Except for the worst case, where the tree is heavily unbalanced with all the nodes being on one side of the tree.
# # In that case, it basically becomes a linked list and the time complexities go up to O(n)

# # Lets implement an unbalanced Binary Search Tree first
# # We will need a node class to store information about each node
# # It will store the data and the pointers to its left and right children

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

# For the insert method, we check if the root node is None, then we make the root node point to the new node
# Otherwise, we create a temporary pointer which points to the root node at first.
# Then we compare the data of the new node to the data of the node pointed by the temporary node.
# If it is greater then first we check if the right child of the temporary node exists, if it does, then we update the temporary node to its right child
# Otherwise we make the new node the right child of the temporary node
# And if the new node data is less than the temporary node data, we follow the same procedure as above this time with the left child.
# The complexity is O(log N) in avg case and O(n) in worst case.

    def insert(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
            return
        else:
            curr_node = self.root
            while True:
                if data < curr_node.data:
                    # Left
                    if curr_node.left == None:
                        curr_node.left = new_node
                        return
                    else:
                        curr_node = curr_node.left
                elif data > curr_node.data:
                    # Right
                    if curr_node.right == None:
                        curr_node.right = new_node
                        return
                    else:
                        curr_node = curr_node.right

# Now we will implement the lookup method.
# It will follow similar logic as to the insert method to reach the correct position.
# Only instead of inserting a new node we will return "Found" if the node pointed by the temporary node contains the same value we are looking for

    def lookup(self, data):
        curr_node = self.root
        while True:
            if curr_node == None:
                return False
            if curr_node.data == data:
                return True
            elif data < curr_node.data:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

    def print_tree(self):
        if self.root != None:
            self.printt(self.root)
# Inorder Traversal (We get sorted order of elements in tree)

    def printt(self, curr_node):
        if curr_node != None:
            self.printt(curr_node.left)
            print(str(curr_node.data))
            self.printt(curr_node.right)


# Remove element from binary search tree do it while doing recursion

bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(6)
bst.insert(12)
bst.insert(8)
bst.insert(2)
x = bst.lookup(6)
print(x)
y = bst.lookup(99)
print(y)
bst.print_tree()
