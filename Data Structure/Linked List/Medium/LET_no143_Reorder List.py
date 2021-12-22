# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        last = None
        cur = slow.next
        slow.next = None
        
        while cur:
            nxt = cur.next
            cur.next = last
            last = cur
            cur = nxt
        
        head2 = head
        while last:
            nxt = head2.next
            head2.next = last
            head2 = head2.next
            last = nxt
        