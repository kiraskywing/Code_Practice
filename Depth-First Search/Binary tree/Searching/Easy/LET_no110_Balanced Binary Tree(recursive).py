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
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):

        result, _ = self.validate(root)
        return result

    def validate(self, root):

        if not root:
            return True, 0

        valid, left_height = self.validate(root.left)
        if not valid:
            return False, 0

        valid, right_height = self.validate(root.right)
        if not valid:
            return False, 0

        return abs(left_height - right_height) <= 1, max(left_height, right_height) + 1