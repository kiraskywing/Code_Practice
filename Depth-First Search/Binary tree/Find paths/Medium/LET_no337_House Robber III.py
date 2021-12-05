# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        cur_not_used, cur_used = self.helper(root)
        return max(cur_not_used, cur_used)
    
    def helper(self, root):
        if not root:
            return 0, 0
        
        left_not_used, left_used = self.helper(root.left)
        right_not_used, right_used = self.helper(root.right)
        
        cur_not_used = max(left_used, left_not_used) + max(right_used, right_not_used)
        cur_used = left_not_used + right_not_used + root.val
        
        return cur_not_used, cur_used
        