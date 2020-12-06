"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        dummy = Node(0)
        nxt = dummy
        
        while cur:
            while cur:
                if cur.left: 
                    nxt.next = cur.left
                    nxt = nxt.next
                if cur.right:
                    nxt.next = cur.right
                    nxt = nxt.next
                cur = cur.next
            cur = dummy.next
            dummy.next = None
            nxt = dummy
        
        return root