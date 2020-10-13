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

        while len(lists) > 1:
            next_lists = []

            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    new_list = self.merge_two_lists(lists[i], lists[i + 1])
                else:
                    new_list = lists[i]
                next_lists.append(new_list)
            lists = next_lists

        return lists[0]

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

        if head_1:
            cur.next = head_1
        if head_2:
            cur.next = head_2

        return dummy.next
