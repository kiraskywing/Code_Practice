# The same as LeetCode no203. Remove Linked List Elements

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):

        dum = ListNode(0, head)
        p = dum
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        return dum.next