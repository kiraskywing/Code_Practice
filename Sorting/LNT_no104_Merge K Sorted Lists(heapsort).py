# The same as LeetCode no.23 Merge k Sorted Lists

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq

ListNode.__lt__ = lambda x, y: (x.val < y.val)


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """

    def mergeKLists(self, lists):
        if not lists:
            return None

        dummy = ListNode(-1)
        cur = dummy
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        while heap:
            head = heapq.heappop(heap)
            cur.next = head
            cur = cur.next
            if head.next:
                heapq.heappush(heap, head.next)

        return dummy.next
