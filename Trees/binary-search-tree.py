# Binary Search Trees are a non-linear data structure.
# They consist of a root node and zero, one or two children where the children can again have 0,1, or 2 nodes as their children and so on
# In most cases, the time complexity of operations on a BST, which include, lookups, insertions and deletions, take O(log N) time
# Except for the worst case, where the tree is heavily unbalanced with all the nodes being on one side of the tree.
# In that case, it basically becomes a linked list and the time complexities go up to O(n)

# Lets implement an unbalanced Binary Search Tree first
# We will need a node class to store information about each node
# It will store the data and the pointers to its left and right children

class Node():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# Now we will implement the Binary Search Tree having a constructor with the root node initialised to None
# And the three methods, lookup, insert and delete


class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

# For the insert method, we check if the root node is None, then we make the root node point to the new node
# Otherwise, we create a temporary pointer which points to the root node at first.
# Then we compare the data of the new node to the data of the node pointed by the temporary node.
# If it is greater then first we check if the right child of the temporary node exists, if it does, then we update the temporary node to its right child
# Otherwise we make the new node the right child of the temporary node
# And if the new node data is less than the temporary node data, we follow the same procedure as above this time with the left child.
# The complexity is O(log N) in avg case and O(n) in worst case.
    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            self.number_of_nodes += 1
            return self
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if not current_node.left:
                        current_node.left = current_node
                        self.number_of_nodes += 1
                        return self
                    else:
                        current_node = current_node.left
                        self.number_of_nodes += 1

                else:
                    if not current_node.right:
                        current_node.right = current_node
                        self.number_of_nodes += 1

                    else:
                        current_node.right = current_node
                        self.number_of_nodes += 1
                        return self
            return
# Now we will implement the lookup method.
# It will follow similar logic as to the insert method to reach the correct position.
# Only instead of inserting a new node we will return "Found" if the node pointed by the temporary node contains the same value we are looking for

    def lookup(self, value):
        if self.root == None:
            return "Tree is Empty"
        else:
            current_node = self.root
            while True:
                if current_node == None:
                    print("Not Found")
                else:
                    while True:
                        if current_node.value == value:
                            return "Found"
                        elif current_node.value > value:
                            current_node = current_node.left
                        else:
                            current_node = current_node.right

    # def remove(self, value):


myBinarySearchTree = BinarySearchTree()
myBinarySearchTree.insert(9)
myBinarySearchTree.insert(20)
myBinarySearchTree.insert(8)
print(myBinarySearchTree)
