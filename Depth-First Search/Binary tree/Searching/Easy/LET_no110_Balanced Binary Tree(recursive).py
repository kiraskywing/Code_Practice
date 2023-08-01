# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res, _ = self.helper(root)
        return res

    def helper(self, root):
        if not root:
            return True, 0

        left_res, left_h = self.helper(root.left)
        right_res, right_h = self.helper(root.right)

        return left_res and right_res and abs(left_h - right_h) <= 1, 1 + max(left_h, right_h)