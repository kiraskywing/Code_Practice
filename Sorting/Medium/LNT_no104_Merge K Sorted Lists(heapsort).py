# The same as LeetCode no.23 Merge k Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        dummy = ListNode(-1)
        cur = dummy
        temp = []
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(temp, (head.val, i))

        while temp:
            val, i = heapq.heappop(temp)
            cur.next = lists[i]
            cur = cur.next
            if cur.next:
                lists[i] = cur.next
                heapq.heappush(temp, (lists[i].val, i))

        return dummy.next
