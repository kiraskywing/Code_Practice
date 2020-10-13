"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """

    def oddEvenList(self, head):

        if not head:
            return head

        odd, even = head, head.next
        evenhead = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenhead

        return head