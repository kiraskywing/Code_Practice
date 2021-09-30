# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        divide, rest = n // k, n % k
        res = []
        last = None
        for _ in range(k):
            res.append(head)
            times = divide + (rest > 0)
            while times and head:
                last = head
                head = head.next
                times -= 1
            rest -= 1
            if last: last.next = None
        return res