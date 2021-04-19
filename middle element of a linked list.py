def middleNode(self, head):
    curr_node = head
    count = 0
    while curr_node:
        curr_node = curr_node.next
        count += 1

    curr = head
    for i in range(count//2):
        curr = curr.next
    return curr
