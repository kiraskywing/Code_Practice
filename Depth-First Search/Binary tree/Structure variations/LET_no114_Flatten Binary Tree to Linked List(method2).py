"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """

    def flatten(self, root):

        self.helper(root)

    def helper(self, root):

        if not root:
            return None

        last_left = self.helper(root.left)
        last_right = self.helper(root.right)

        if last_left:
            last_left.right = root.right
            root.right = root.left
            root.left = None

        if last_right:
            return last_right

        if last_left:
            return last_left

        return root