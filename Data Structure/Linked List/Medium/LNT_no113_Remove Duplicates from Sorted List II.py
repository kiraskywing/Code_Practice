# The same as Leetcode no82_Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1000)
        dummy.next = head
        prev = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                value = head.val
                while head and head.val == value:
                    head = head.next
                prev.next = head
            else:
                prev, head = prev.next, head.next
        
        return dummy.next