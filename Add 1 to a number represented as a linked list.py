def addOne(head):

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

    while l1 != None or carry:
        if l1:
            carry += l1.data

        l1.data = carry % 10

        carry = carry // 10

        if l1.next == None and carry == 1:
            l1.next = Node(0)
            l1 = l1.next
        else:
            l1 = l1.next

    return reverse(head)
