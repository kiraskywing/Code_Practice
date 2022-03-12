# The same as LeetCode no138. Copy List with Random Pointer

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        memo = {head : Node(head.val)}
        cur = head
        while cur:
            if cur.next not in memo:
                memo[cur.next] = Node(cur.next.val) if cur.next else None
            memo[cur].next = memo[cur.next]
            if cur.random not in memo:
                memo[cur.random] = Node(cur.random.val) if cur.random else None
            memo[cur].random = memo[cur.random]
            cur = cur.next
        
        return memo[head]
