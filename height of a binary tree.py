'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
        '''


class Solution:
    def height(self, root):
        # code here
        if root == None:
            return -1
        lh = self.height(root.left)
        rh = self.height(root.right)
        if lh > rh:
            return lh + 1
        else:
            return rh + 1
