# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        tail = dummy
        
        for _ in range(n):
            tail = tail.next
            
        cur = dummy
        while tail.next:
            cur, tail = cur.next, tail.next
        
        cur.next = cur.next.next
        
        return dummy.next