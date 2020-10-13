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
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        if not head:
            return None

        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        node1, node2 = None, None

        while pre.next:
            if pre.next.val == v1:
                pre1 = pre
                node1 = pre.next
                next1 = node1.next
            if pre.next.val == v2:
                pre2 = pre
                node2 = pre.next
                next2 = node2.next
            if node1 and node2:
                break
            pre = pre.next

        if not node1 or not node2:
            return head

        if node1.next == node2:
            pre1.next = node2
            node2.next = node1
            node1.next = next2
        elif node2.next == node1:
            pre2.next = node1
            node1.next = node2
            node2.next = next1
        else:
            pre1.next = node2
            node2.next = next1
            pre2.next = node1
            node1.next = next2
        return dummy.next