# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head and not head.next:
            return True
        
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        
        cur = slow.next
        last = None
        while cur:
            temp = cur.next
            cur.next = last
            last = cur
            cur = temp
            
        while head and last and head.val == last.val:
            head, last = head.next, last.next
        
        return last is None