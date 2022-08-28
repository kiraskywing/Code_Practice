# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m, n = self.getSize(headA), self.getSize(headB)
        if n > m:
            headA, headB = headB, headA
            m, n = n, m
        
        for _ in range(m - n):
            headA = headA.next
        
        while headA is not headB:
            headA, headB = headA.next, headB.next
        
        return headA
        
    def getSize(self, head):
        size = 0
        while head:
            head = head.next
            size += 1
        return size