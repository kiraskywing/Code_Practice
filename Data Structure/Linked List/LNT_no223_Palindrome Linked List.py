# The same as LeetCode no234. Palindrome Linked List

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):

        if not head or not head.next:
            return True

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        cur, last = slow.next, None

        while cur:
            nxt = cur.next
            cur.next = last
            last, cur = cur, nxt

        while last:
            if last.val != head.val:
                return False
            last = last.next
            head = head.next

        return True

        """
        rec = []

        while head:
            rec.append(head.val)
            head = head.next

        return rec == rec[::-1]
        """