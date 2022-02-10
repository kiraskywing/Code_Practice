# The same as Leetcode no98. Validate Binary Search Tree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):

        return self.validate(root, float('-inf'), float('inf'))

    def validate(self, root, floor, ceiling):
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False

        return self.validate(root.left, floor, root.val) and self.validate(root.right, root.val, ceiling)