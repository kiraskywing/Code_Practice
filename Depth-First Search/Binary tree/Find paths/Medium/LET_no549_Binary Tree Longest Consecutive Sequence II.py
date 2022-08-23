# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        incr, decr, res = self.helper(root)
        return res
        
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        incr = decr = 1
        left_incr, left_decr, left_res = self.helper(root.left)
        right_incr, right_decr, right_res = self.helper(root.right)
        
        if root.left:
            if root.left.val == root.val + 1:
                incr = left_incr + 1
            if root.left.val == root.val - 1:
                decr = left_decr + 1
        if root.right:
            if root.right.val == root.val + 1:
                incr = max(incr, right_incr + 1)
            if root.right.val == root.val - 1:
                decr = max(decr, right_decr + 1)
        
        return incr, decr, max(left_res, right_res, incr + decr - 1)
        