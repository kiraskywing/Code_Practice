# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        memo = collections.defaultdict(int)
        cur = head
        while cur:
            memo[cur.val] += 1
            cur = cur.next
            
        dummy = ListNode(-1, head)
        prev, cur = dummy, dummy.next
        
        while cur:
            while cur and memo[cur.val] > 1:
                cur = cur.next
            prev.next = cur
            if cur:
                prev, cur = cur, cur.next
        
        return dummy.next