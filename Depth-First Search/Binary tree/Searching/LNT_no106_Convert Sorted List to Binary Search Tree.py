"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """

    def sortedListToBST(self, head):

        return self.convert(head)

    def convert(self, head):

        if not head:
            return
        if not head.next:
            return TreeNode(head.val)

        dummy = ListNode(-1, head)
        slow, fast = dummy, head

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow.next
        slow.next = None
        root = TreeNode(mid.val)

        root.left = self.convert(head)
        root.right = self.convert(mid.next)

        return root
