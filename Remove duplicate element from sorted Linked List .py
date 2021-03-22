
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


# Function to remove duplicates from sorted linked list.


def removeDuplicates(head):
    # code here
    while head.next == None:
        return head

    while head.next:
        if head.data == head.next.data:
            head.next = head.next.next
        else:
            head = head.next
    return head
