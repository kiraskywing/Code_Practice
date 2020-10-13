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
    @return: Head node.
    """
    def removeDuplicates(self, head):

        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        rec = set()

        while cur.next:
            if cur.next.val not in rec:
                rec.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next

        return dummy.next