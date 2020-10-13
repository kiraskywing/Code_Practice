"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: the first node of linked list.
    @return: An integer
    """
    def countNodes(self, head):
        value = 0
        while head:
            value += 1
            head = head.next

        return value

        """
        if not head:
            return 0

        return self.countNodes(head.next) + 1
        """