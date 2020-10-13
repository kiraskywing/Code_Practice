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
    @return: head of the linked list
    """
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        tmp = dummy
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                rec = cur.val
                while cur and cur.val == rec:
                    cur = cur.next
                tmp.next = cur
            else:
                tmp = tmp.next
                cur = cur.next

        return dummy.next