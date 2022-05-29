"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            cur = Node(insertVal)
            cur.next = cur
            return cur
        
        prev, nxt = head, head.next
        cur = Node(insertVal)
        while prev.next is not head:
            if prev.val <= cur.val <= nxt.val:
                break
            if prev.val > nxt.val and (cur.val > prev.val or cur.val < nxt.val):
                break
            prev, nxt = prev.next, nxt.next
            
        prev.next = cur
        cur.next = nxt
        
        return head