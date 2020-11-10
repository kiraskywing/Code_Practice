# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0
        return self.dfs(root, root.val, root.val)
    
    def dfs(self, root, high, low):
        if not root:
            return high - low
        
        high = max(high, root.val)
        low = min(low, root.val)
        return max(self.dfs(root.left, high, low), self.dfs(root.right, high, low))