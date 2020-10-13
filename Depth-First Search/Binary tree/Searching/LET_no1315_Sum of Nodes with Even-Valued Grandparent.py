# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        return self.get_valueSum(root, 1, 1)

    def get_valueSum(self, root, par_val, grand_val):
        if not root:
            return 0
        return self.get_valueSum(root.left, root.val, par_val) + self.get_valueSum(root.right, root.val, par_val) + root.val * (1 - grand_val % 2)