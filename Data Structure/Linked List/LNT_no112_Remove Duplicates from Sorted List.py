"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: head is the head of the linked list
    @return: head of linked list
    """
    def deleteDuplicates(self, head):

        if not head:
            return head

        cur = head

        while cur and cur.next:
            if cur.val != cur.next.val:
                cur = cur.next
            else:
                cur.next = cur.next.next

        return head