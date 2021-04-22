class Solution:
    def isPalindrome(self, head):

        temp = []
        while head.next:
            temp.append(head.val)
            head = head.next

        temp.append(head.val)

        if temp == temp[::-1]:
            return True
        return False
