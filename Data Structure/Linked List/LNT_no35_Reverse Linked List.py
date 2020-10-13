"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        cur, nex = None, None

        while head:
            nex = head.next
            head.next = cur
            cur = head
            head = nex

        return cur