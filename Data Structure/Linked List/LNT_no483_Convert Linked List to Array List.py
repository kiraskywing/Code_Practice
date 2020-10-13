"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param {ListNode} head the first node of the linked list.
    @return {int[]} an integer list
    """
    def toArrayList(self, head):

        res = []

        while head:
            res.append(head.val)
            head = head.next

        return res