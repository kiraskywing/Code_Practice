# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []    # Space: O(h) where h is the tree's height
        while root:    # Time: O(h)
            stack.append(root)
            root = root.left
            
        res = None
        for _ in range(k):    # Time: O(k)
            cur = stack.pop()
            res = cur.val
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        
        return res