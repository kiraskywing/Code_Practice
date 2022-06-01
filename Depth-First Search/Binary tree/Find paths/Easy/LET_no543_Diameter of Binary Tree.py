# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res, _ = self.dfs(root)
        return res
    
    def dfs(self, cur):
        if not cur:
            return 0, 0
        
        leftRes, leftMax = self.dfs(cur.left)
        rightRes, rightMax = self.dfs(cur.right)
        
        return max(leftRes, rightRes, leftMax + rightMax), max(leftMax, rightMax) + 1