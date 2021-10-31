"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        cur = head
        while cur:
            if cur.child:
                nxt = cur.next
                cur.next = cur.child
                cur.child = None
                cur.next.prev = cur
                nxt2 = cur.next
                while nxt2.next:
                    nxt2 = nxt2.next
                nxt2.next = nxt
                if nxt:
                    nxt.prev = nxt2
            cur = cur.next
        return head