# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = 0
        queue = collections.deque([(root, 1)])
        while queue:
            left, right = float('inf'), float('-inf')
            for _ in range(len(queue)):
                cur, idx = queue.popleft()
                left, right = min(left, idx), max(right, idx)
                if cur.left:
                    queue.append((cur.left, idx * 2))
                if cur.right:
                    queue.append((cur.right, idx * 2 + 1))
            res = max(res, right - left + 1)
        
        return res