def addTwoLists(first, second):
    # code here
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

    head = l3 = Node(0)
    l1 = reverse(first)
    l2 = reverse(second)
    carry = 0

    while l1 or l2 or carry:

        if l1:
            carry += l1.data
            l1 = l1.next
        if l2:
            carry += l2.data
            l2 = l2.next

        l3.data = carry % 10
        carry = carry // 10

        if l1 or l2 or carry:
            l3.next = Node(0)
            l3 = l3.next

    return reverse(head)
