def getNthFromLast(head, n):

    def reverse(head):
        if not head:
            return
        first = head
        second = first.next
        first.next = None
        while second:
            third = second.next
            second.next = first
            first = second
            second = third
        return first

    head = reverse(head)
    count = 1

    while head:
        if count == n:
            return head.data
        head = head.next
        count += 1

    return -1
