# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        _, res = self.helper(root)
        return res

    def helper(self, root):
        if not root:
            return 0, 0

        left_longest, left_res = self.helper(root.left)
        right_longest, right_res = self.helper(root.right)

        cur_left = cur_right = 0
        if root.left and root.left.val == root.val:
            cur_left = left_longest + 1
        if root.right and root.right.val == root.val:
            cur_right = right_longest + 1
        cur_res = cur_left + cur_right

        return max(cur_left, cur_right), max(cur_res, left_res, right_res)