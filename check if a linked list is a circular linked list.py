def isCircular(head):
    static_node = head
    moving_node = head

    while moving_node:
        moving_node = moving_node.next
        if moving_node == static_node:
            return 1
    return 0
