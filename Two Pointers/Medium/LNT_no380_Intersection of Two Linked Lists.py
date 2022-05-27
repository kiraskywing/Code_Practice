# The same as LeetCode no.160 Intersection of Two Linked Lists

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        m, n = self.getSize(headA), self.getSize(headB)
        if n > m:
            return self.helper(headB, headA, n - m)
        return self.helper(headA, headB, m - n)
        
    def getSize(self, node):
        size = 0
        while node:
            size += 1
            node = node.next
        return size
    
    def helper(self, node1, node2, diff):
        for _ in range(diff):
            node1 = node1.next
        
        while node1 and node2 and node1 is not node2:
            node1, node2 = node1.next, node2.next
        return node1