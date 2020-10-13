"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2
    """
    def addLists(self, l1, l2):

        dummy = ListNode(-1)
        cur = dummy
        adder = False

        while True:
            val = 0
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            if adder:
                val += 1
            cur.next = ListNode(val % 10)
            cur = cur.next

            if val >= 10:
                adder = True
            else:
                adder = False
            if not l1 and not l2:
                break

        if adder:
            cur.next = ListNode(1)

        return dummy.next
