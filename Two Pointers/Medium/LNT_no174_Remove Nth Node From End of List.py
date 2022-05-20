# The same as LeetCode no19. Remove Nth Node From End of List

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):

        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, head

        for i in range(n):
            fast = fast.next

        while fast:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next

        return dummy.next
