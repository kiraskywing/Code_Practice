# The same as LintCode no1172_Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        res, _ = self.dfs(root)
        return res
    
    def dfs(self, root):
        if not root:
            return 0, 0
        left_diff, left_total = self.dfs(root.left)
        right_diff, right_total = self.dfs(root.right)
        return left_diff + right_diff + abs(left_total - right_total), left_total + right_total + root.val