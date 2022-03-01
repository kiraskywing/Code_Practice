"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        memo = {root : Node(root.val)}
        queue = collections.deque([root])
        while queue:
            cur = queue.popleft()
            for child in cur.children:
                if child not in memo:
                    memo[child] = Node(child.val)
                queue.append(child)
                memo[cur].children.append(memo[child])
        
        return memo[root]