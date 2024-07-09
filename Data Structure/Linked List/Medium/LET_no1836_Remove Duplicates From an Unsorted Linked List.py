# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        memo = collections.defaultdict(int)
        cur = head
        while cur:
            memo[cur.val] += 1
            cur = cur.next

        dummy = ListNode(-1, head)
        cur = dummy
        while cur.next:
            if memo[cur.next.val] > 1:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next