# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = collections.deque([(None, root)])
        while queue:
            parent = 0
            for _ in range(len(queue)):
                p, c = queue.popleft()
                if p and (c.val == x or c.val == y):
                    if not parent: parent = p.val
                    else: return parent != p.val
                if c.left: queue.append((c, c.left))
                if c.right: queue.append((c, c.right))
        return False