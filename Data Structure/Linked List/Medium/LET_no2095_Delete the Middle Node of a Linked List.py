# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev = cur = dummy
        while cur.next and cur.next.next:
            cur = cur.next.next
            prev = prev.next
        
        prev.next = prev.next.next
        
        return dummy.next