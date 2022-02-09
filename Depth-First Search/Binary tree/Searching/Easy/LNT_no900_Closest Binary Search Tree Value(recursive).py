"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """

    def closestValue(self, root, target):

        upper = self.get_upper(root, target)
        lower = self.get_lower(root, target)

        if not upper:
            return lower.val
        if not lower:
            return upper.val

        if upper.val - target >= target - lower.val:
            return lower.val
        else:
            return upper.val

    def get_upper(self, root, target):

        if not root:
            return None

        if root.val <= target:
            return self.get_upper(root.right, target)

        upper = self.get_upper(root.left, target)

        return root if not upper else upper

    def get_lower(self, root, target):

        if not root:
            return None

        if root.val > target:
            return self.get_lower(root.left, target)

        lower = self.get_lower(root.right, target)

        return root if not lower else lower