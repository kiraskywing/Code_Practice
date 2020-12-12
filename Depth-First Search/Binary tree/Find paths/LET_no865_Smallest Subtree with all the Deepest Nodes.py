# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        res, _ = self.dfs(root)
        return res
    
    def dfs(self, root):
        if not root:
            return None, 0
        
        left_res, left_depth = self.dfs(root.left)
        right_res, right_depth = self.dfs(root.right)
        
        if left_depth > right_depth:
            return left_res, left_depth + 1
        elif left_depth < right_depth:
            return right_res, right_depth + 1
        else:
            return root, left_depth + 1