# Reversing a linked list.
# We'll take the whole same code from implementation of a linked list file and add a reverse method.

from implementation import LinkedList, Node

# Now we create a Linked List by appending some values
myLinkedList = LinkedList()
myLinkedList.append(5)
myLinkedList.append(8)
myLinkedList.append(10)
myLinkedList.append(99)
myLinkedList.append(20)
print(myLinkedList)

# 5 8 10 99 20

# Iterative


def reverse(self):
    if self.length == 1:  # Check if length of linked list is 1 then only one element is present and we dont need to reverse the linked list
        # Return the first element of the linked list if only one element is present.
        return self.head
    else:  # If more than one element is present then following are the steps to reverse the linked list.
        # Suppose we have a linked list 5 8 10 99 20 , we are assigning variable first = 5.
        first = self.head
        self.tail = self.head  # we are making the tail of the linked list = 5.
        second = first.next  # we are making the variable second = 8
        # if the variable second is not null (which would be true if the length would be 1 and next property of the head would be null).
        while second:
            # we are initalizing a variable temp = 10, so now we have first = 5 , second = 8 and temp = 10
            temp = second.next
            # we are making the next property of 8 point to 5.
            second.next = first
            # we are making 8 as the first element after making it point to 5 . so here first = 8.
            first = second
            second = temp  # we are making the variable second = 10.
        self.head.next = None  # we make the pointer of the head of the linked list equal to null
        # when the loop finishes its run first will be equal to 20 and we'll make it as the head of the linked list.
        self.head = first
    return self  # We return the linked list


# def ReverseRecursive(self, node: Node, prev: Node = None) -> Node:
#     if not self.node:
#         return prev
#     else:
#         self.next = self.node.next
#         self.node.next = self.prev
#         return ReverseRecursive(self.next, self.node)
#     # return ReverseRecursive(self.head)


LinkedList = reverse(myLinkedList)
# LinkedList = ReverseRecursive(myLinkedList.head, None)
print(LinkedList)
