"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        return self.merge_range_lists(lists, 0, len(lists) - 1)

    def merge_range_lists(self, lists, left, right):
        if left >= right:
            return lists[left]

        mid = (left + right) // 2

        merged_left = self.merge_range_lists(lists, left, mid)
        merged_right = self.merge_range_lists(lists, mid + 1, right)
        return self.merge_two_lists(merged_left, merged_right)

    def merge_two_lists(self, head_1, head_2):
        dummy = ListNode(-1)
        cur = dummy

        while head_1 and head_2:
            if head_1.val < head_2.val:
                cur.next = head_1
                head_1 = head_1.next
            else:
                cur.next = head_2
                head_2 = head_2.next
            cur = cur.next

        cur.next = head_1 if head_1 else head_2

        return dummy.next
