from implementation import LinkedList, Node

# Now we create a Linked List by appending some values
myLinkedList = LinkedList()
myLinkedList.append(5)
myLinkedList.append(8)
myLinkedList.append(10)
myLinkedList.append(99)
myLinkedList.append(20)
print(myLinkedList)


def hasCycle(self, head: Node) -> bool:
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False
