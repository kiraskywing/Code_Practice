# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        cur = dummy
        nxt_digit = 0
        
        while l1 or l2:
            value = nxt_digit
            if l1:
                value += l1.val
                l1 = l1.next
            if l2:
                value += l2.val
                l2 = l2.next
            cur.next = ListNode(value % 10)
            nxt_digit = value // 10
            cur = cur.next
        if nxt_digit:
            cur.next = ListNode(nxt_digit)
        
        return dummy.next