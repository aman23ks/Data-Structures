def compute(head):
    # Your code here
    def reverse(head):
        if head.next == None:
            return head

        first = head
        second = first.next
        first.next = None
        while second:
            third = second.next
            second.next = first
            first = second
            second = third

        return first

    head = prev = reverse(head)
    ma = prev.data
    curr = prev.next
    while curr:
        if curr.data >= ma:
            ma = curr.data
            curr = curr.next
            prev = prev.next
        else:
            prev.next = curr.next
            curr = curr.next

    return reverse(head)
