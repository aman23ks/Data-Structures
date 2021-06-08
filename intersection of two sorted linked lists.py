class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findIntersection(head1, head2):
    l1 = head1
    l2 = head2
    head = Node(None)
    curr = Node(None)

    while l1 and l2:
        if l1.data == l2.data:
            if head.data == None:
                t = Node(l1.data)
                head = t
                curr = t
            else:
                t = Node(l1.data)
                curr.next = t
                curr = curr.next

            l1 = l1.next
            l2 = l2.next

        else:
            if l1.data > l2.data:
                l2 = l2.next
            else:
                l1 = l1.next

    return head
