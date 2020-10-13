"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @param val: An integer.
    @return: The head of new linked list.
    """
    def insertNode(self, head, val):

        if not head:
            return ListNode(val)

        dummy = ListNode(-1, head)
        cur = dummy

        while cur.next and cur.next.val < val:
            cur = cur.next

        node = ListNode(val, cur.next)
        cur.next = node

        return dummy.next