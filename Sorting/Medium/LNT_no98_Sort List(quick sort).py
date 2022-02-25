"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):

        if not head or not head.next:
            return head

        mid = self.find_mid(head)

        dummy_left = ListNode(-1)
        dummy_middle = ListNode(-1)
        dummy_right = ListNode(-1)

        cur_left = dummy_left
        cur_middle = dummy_middle
        cur_right = dummy_right

        while head:

            if head.val < mid.val:
                cur_left.next = head
                cur_left = cur_left.next
            elif head.val == mid.val:
                cur_middle.next = head
                cur_middle = cur_middle.next
            else:
                cur_right.next = head
                cur_right = cur_right.next

            head = head.next

        cur_left.next = None
        cur_middle.next = None
        cur_right.next = None

        sorted_left = self.sortList(dummy_left.next)
        sorted_right = self.sortList(dummy_right.next)

        return self.connect(sorted_left, dummy_middle.next, sorted_right)

    def find_mid(self, node):

        if not node or not node.next:
            return node

        slow, fast = node, node

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow.next

    def connect(self, left, middle, right):

        dummy = ListNode(-1)
        cur = dummy

        cur.next = left
        while cur.next:
            cur = cur.next

        cur.next = middle
        while cur.next:
            cur = cur.next

        cur.next = right

        return dummy.next