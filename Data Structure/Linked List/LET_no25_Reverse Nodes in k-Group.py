# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        jump = dummy
        left = right = dummy.next
        
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1
            if count == k:
                pre, cur = right, left
                for _ in range(k):
                    nxt = cur.next
                    cur.next = pre
                    pre = cur
                    cur = nxt
                jump.next = pre
                jump = left
                left = right
            else:
                return dummy.next