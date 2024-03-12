# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        memo = dict()
        memo[0] = dummy = ListNode(0, head)
        
        cur = dummy.next
        prefix = 0
        while cur:
            prefix += cur.val
            memo[prefix] = cur
            cur = cur.next
        
        cur = dummy
        prefix = 0
        while cur:
            prefix += cur.val
            cur.next = memo[prefix].next
            cur = cur.next
        
        return dummy.next
