# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        
        cur = head
        length = 1
        while cur.next:
            cur = cur.next
            length += 1
        
        k %= length
        cur.next = head
        temp = head
        
        for _ in range(length - k - 1):
            temp = temp.next
        ans = temp.next
        temp.next = None
        
        return ans