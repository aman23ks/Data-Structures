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


# Now we implement the BFS method.


    def BFS(self):
        current_node = self.root  # We start with the root node
        BFS_result = []  # This will store the result of the BFS
        queue = []  # Queue to keep track of the children of each node
        queue.append(current_node)  # We add the root to the queue first
        while len(queue) > 0:
            # We extract the first element of the queue and make it the current node
            current_node = queue.pop(0)
            # We push the data of the current node to the result list as we are currently visiting the current node
            BFS_result.append(current_node.data)
            if current_node.left:  # If left child of the current node exists, we append it to the queue
                queue.append(current_node.left)
            if current_node.right:  # Similarly, if right child exists, we append it to the queue
                queue.append(current_node.right)
        return BFS_result

    def BFSRecursive(self, queue, BFS_list):
        if len(queue) == 0:
            return BFS_list
        else:
            current_node = queue.pop(0)
            BFS_list.append(current_node.data)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
            return self.BFSRecursive(queue, BFS_list)

# Now we'll implementthe three kinds of DFS Traversals.

    def DFS_Inorder(self):
        return inorder_traversal(self.root, [])

    def DFS_Preorder(self):
        return preorder_traversal(self.root, [])

    def DFS_Postorder(self):
        return postorder_traversal(self.root, [])


def inorder_traversal(node, DFS_list):
    if node.left:
        inorder_traversal(node.left, DFS_list)
    DFS_list.append(node.data)
    if node.right:
        inorder_traversal(node.right, DFS_list)
    return DFS_list

# check alternate method for recursion and iteration


def preorder_traversal(node, DFS_list):
    DFS_list.append(node.data)
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    return DFS_list


def postorder_traversal(node, DFS_list):
    if node.left:
        preorder_traversal(node.left, DFS_list)
    if node.right:
        preorder_traversal(node.right, DFS_list)
    DFS_list.append(node.data)
    return DFS_list

# # def print_tree(self):
#     #     if self.root != None:
#     #         self.printt(self.root)
# # Inorder Traversal (We get sorted order of elements in tree)


# def printt(self, curr_node, list):
#     if curr_node != self.root:
#         if curr_node.left:
#             printt(curr_node, list)
#         list.append(curr_node.data)
#         if curr_node.right:
#             printt(curr_node, list)


# Inorder - LNR
# Preorder - NLR
# Postorder - LRN


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
# bst.printt([bst.root], [])
print(bst.BFS())
print(bst.BFSRecursive([bst.root], []))
print(bst.DFS_Inorder())
print(bst.DFS_Preorder())
print(bst.DFS_Postorder())
