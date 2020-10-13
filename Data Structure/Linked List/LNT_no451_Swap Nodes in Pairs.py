"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):

        if not head or not head.next:
            return head

        dummy = ListNode(-1)
        cur = dummy

        while head and head.next:
            tmp = head.next.next
            cur.next = head.next
            cur.next.next = head
            cur = cur.next.next
            cur.next = tmp
            head = tmp

        return dummy.next

        """
        dummy = ListNode(-1, head)
        cur = dummy

        while cur.next and cur.next.next:
            tmp = cur.next.next             # tmp equal to 2
            cur.next.next = tmp.next        # 1.next to 3
            tmp.next = cur.next             # 2.next to 1
            cur.next = tmp                  # previous linked to 2->1
            cur = cur.next.next             # move 2 steps

        return dummy.next
        """