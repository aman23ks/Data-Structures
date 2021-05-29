class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


def addOne(head):
    # Returns new head of linked List.

    def reverse(head):
        if head.next == None:
            return head

        else:
            first = head
            second = head.next
            first.next = None
            while second:
                temp = second.next
                second.next = first
                first = second
                second = temp

        return first

    carry = 1
    head = l1 = reverse(head)

    # 0 -> 0 -> 0 -> 1

    # 1 -> 0 -> 0 -> 0

    while l1 or carry:
        if l1:
            carry += l1.val

        l1.val = carry % 10
        carry = carry // 10

        l1 = l1.next

        if l1.next == None and carry == 1:
            l1.next = Node(0)
            l1 = l1.next
    return reverse(l1)
