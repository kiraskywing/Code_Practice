# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        t1 = t2 = head
        for i in range(k - 1):
            t1 = t1.next
        t3 = t1
        while t3.next:
            t3, t2 = t3.next, t2.next
        t1.val, t2.val = t2.val, t1.val
        
        return head