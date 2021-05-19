def removeDuplicates(self, head):

    if not head:
        return None
    # code here
    # return head after editing list
    hashmap = {}
    prev = head
    curr = prev.next
    hashmap[prev.data] = 1

    while curr:
        if curr.data not in hashmap:
            hashmap[curr.data] = 1
            prev = curr
            curr = curr.next
        else:
            prev.next = curr.next
            curr = curr.next

    return head
