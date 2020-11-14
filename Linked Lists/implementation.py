# Linked lists are, as the name suggests, a list which is linked.
# It consists of nodes which contain data and a pointer to the next node in the list.
# The list is connected with the help of these pointers.
# These nodes are scattered in memory, quite like the buckets in a hash table.
# The node where the list starts is called the head of the list and the node where it ends, or last node, is called the tail of the list.
# The average time complexity of some operations invloving linked lists are as follows:
# Look-up : O(n)
# Insert : O(n)
# Delete : O(n)
# Append : O(1)
# Prepend : O(1)
# Python doesn't have a built-in implementation of linked lists, we have to build it on our own
# So, here we go.

# Lets create a linked list with the following example: 5 --> 10 --> 16

# The structure we are essentially trying to obtain is the one below.

# myLinkedList = {
#     "head": {
#         "value": 5,
#         "next": {
#             "value": 10,
#             "next": {
#                 "value": 16,
#                 "next": None
#             }
#         }
#     }
# }

# Creating the above linked list using classes and objects.

# First we define as a class node which will act as a blueprint for each of our nodes.
class Node():
    # When instiniating a node we will pass the data we want the node to hold.
    def __init__(self, data):
        self.data = data  # The data passed during instintiation will be stored in self.data
        # This self.next will act as a pointer to the next node in the list. When creating a new node, it always points to null(or None).
        self.next = None


# Next we define the class LinkedList which will have a head pointer to point to the beginning of the list and a tail pointer to
# point to the end of the list. An optional value of length can also be stored to keep track of the length of the linked list.
# When the list is created , it is empty and there is no node to point to. So head will point to None at the time of creation of linked list
# And since the list is empty at the time of creation, we will point the tail to whatever the head is pointing to, i.e., None
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

# Next operation we'll implement is prepend, wehre we add a node at the head of the list.
# For this, we will call the prepend method and pass the value we want to enter, which will create a new object of the node class
# Then we will make the 'next' of the new node point to the head ,as the head is currently pionting to the first node of the list
# And then we will update the head to point to new node as we want the new node to be new first node, i.e, the new head.
# And ofcourse, we'll increase the length by 1
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

# Now we will implement the print function to print the values in the nodes of the linked list
# We will check if the list is empty or not. If it is, we will printout "Empty"
# Else, we will create a new node which will point to the head. Then we will loop until the node we created becomes None
# Inside the loop we will print the data of the current node and then make the current node equal to the node pointed by the current node
# Since this requires us to traverse the entire lenth of the linked list, this is an O(n) operation.

    # __str__ tells the print statement what to print, only then linked list can be printed.
    def __str__(self):
        if self.head == None:
            return "Empty"
        else:
            values = ""
            current_node = self.head
            while current_node != None:
                values += str(current_node.data)
                values += " "
                current_node = current_node.next
        return values


# Next comes the insert operation, where we insert a data at a specified position
# If the position is greater than the length of the list, we simply follow the procedure of the append method where we add the node to the end of the list
# If the position is equal to 0, we follow the prepend procedure, where we append the node at the head
# If the postition is somewhere in between, then we create a temporary node which traverses the list upto the previous position of the position we want to enter the new node
# Now the 'next' of the temporary node is pointing to the next node in the list, wehre we want to insert our new node
# So first we link the new node and the node at the desired position by making the 'next' of the new node equal to the 'next' of the temporary node
# The temporary node and the new node point to the same position now, the position we want to insert the new node
# So we update the 'next' of the temporary node to point to the new node.
# This way, our new node occupies the position it intended to and the node which was originally there, gets pushed to the next position
# Since this requires traversal of the list, it is an O(n) operation.


    def insert(self, index, data):
        new_node = Node(data)
        if index >= self.length:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.length += 1
        else:
            current_node = self.head
            for i in range(index-1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

# Next comes the delete_by_value method where the user can enter a value and if the value is found in the list, it will be deleted.
# (If the value is found multiple times, only the first occurence of thevalue will be deleted.)
# First we check if the list is empty. If yes, we print appropriate message. If not, then we create a temporary node.
# Then we check if the value of the head is equal to the value we want deleted.
# If yes, we make the head equal to the node pointed by the 'next' of the head. Then we check if there are only one or zero nodes in the list
# If yes, then we update the tail to be equal to the head.
# By Doing this, the original 'head' gets disconnected from the list and the head becomes updated to what was originally the second node
# If these two cases are not encountered, then we have to traverse the list and check every node.
# So we loop until either the current node becomes None, signifying the end of the list, or until the data of the node next to the current node equals the data we want deleted.
# After coming out of the loop we check if the current node is not equal to None, it means the next node of the current node is the one we want deleted
# So we make the 'next' of the current node point to the next to the next of the current node.
# Effectively, we bypass the node we want deleted and establish a connection between the current and the next to next of the current nodes.
# After deleting the required node, we check if the current node's 'next' points to None, i.e., if it is the last node. If yes, then we update the tail
# And if the current node is None, it means we traversed the entire list but couldn't find the value.
# Time complexity is pretty clearly O(n)
    def remove(self, index):
        if self.head == None:
            print("Linked List is Empty nothing to delete")
        else:
            preceding_node = self.head
            succedding_node = self.head
            for i in range(index-1):
                preceding_node = preceding_node.next
            for i in range(index+1):
                succedding_node = succedding_node.next
            preceding_node.next = succedding_node
            self.length -= 1


# myLinkedList = LinkedList()
# myLinkedList.append(5)
# myLinkedList.append(8)
# myLinkedList.append(10)
# myLinkedList.append(99)
# myLinkedList.append(20)
# myLinkedList.insert(3, 30)
# myLinkedList.remove(5)
# myLinkedList.remove(3)
# print(myLinkedList)
