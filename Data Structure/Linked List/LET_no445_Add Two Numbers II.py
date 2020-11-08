# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp1, temp2 = [], []
        while l1:
            temp1.append(l1.val)
            l1 = l1.next
        while l2:
            temp2.append(l2.val)
            l2 = l2.next
        
        total = 0
        cur = ListNode(0)
        while temp1 or temp2:
            if temp1: total += temp1.pop()
            if temp2: total += temp2.pop()
            cur.val = total % 10
            head = ListNode(total // 10)
            head.next = cur
            cur = head
            total //= 10
        
        return head if total != 0 else head.next
            