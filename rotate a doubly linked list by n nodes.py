

def update(llist, p):
    if p == 0:
        return llist

    count = 1
    head = llist.head
    next_val = llist.head.next
    while next_val:
        if count == p:
            val = new_head = next_val
            next_val.prev.next = None
            new_head.prev = None
        next_val = next_val.next
        count += 1

    while new_head.next != None:
        new_head = new_head.next

    new_head.next = head
    head.prev = new_head
    return val.data


print(update(myDoublyLinkedList, 1))
