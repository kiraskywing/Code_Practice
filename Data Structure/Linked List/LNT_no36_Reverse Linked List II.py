"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        pre1 = dummy

        for _ in range(m - 1):
            pre1 = pre1.next

        cur = pre1.next
        last = None
        pre2 = cur

        for _ in range(n - m + 1):
            next_head = cur.next
            cur.next = last
            last = cur
            cur = next_head

        pre1.next = last
        pre2.next = cur

        return dummy.next
