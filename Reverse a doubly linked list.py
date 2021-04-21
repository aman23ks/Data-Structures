def reverseDLL(head):
    # return head after reversing
    while head.next != None:
        head.prev, head.next, head = head.next, head.prev, head.next

    head.prev, head.next = None, head.prev

    return head
