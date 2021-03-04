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
        lenA, lenB = 0, 0
        nodeA, nodeB = headA, headB
        while nodeA:
            lenA += 1
            nodeA = nodeA.next
        while nodeB:
            lenB += 1
            nodeB = nodeB.next

        nodeA, nodeB = headA, headB
        while lenA > lenB:
            nodeA = nodeA.next
            lenA -= 1
        while lenB > lenA:
            nodeB = nodeB.next
            lenB -= 1

        while nodeA and nodeB and nodeA.val != nodeB.val:
            nodeA = nodeA.next
            nodeB = nodeB.next
        return nodeA