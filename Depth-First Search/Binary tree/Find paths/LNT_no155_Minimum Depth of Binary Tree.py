"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root):
        if not root:
            return 0

        min_depth = self.get_depth(root)
        return min_depth

    def get_depth(self, root):

        if root.left and root.right:
            left_depth = self.get_depth(root.left)
            right_depth = self.get_depth(root.right)
            return min(left_depth, right_depth) + 1

        elif root.left:
            return self.get_depth(root.left) + 1
        elif root.right:
            return self.get_depth(root.right) + 1
        else:
            return 1



