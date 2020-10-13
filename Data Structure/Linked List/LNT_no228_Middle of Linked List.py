# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        if not head or not head.next:
            return head

        slow, fast = head, head

        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next

        if fast.next:
            return slow.next
        else:
            return slow