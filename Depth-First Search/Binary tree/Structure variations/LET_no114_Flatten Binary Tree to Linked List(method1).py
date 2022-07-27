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

        self.last_node = None
        self.helper(root)

    def helper(self, root):

        if not root:
            return

        if self.last_node:
            self.last_node.left = None
            self.last_node.right = root

        self.last_node = root
        right = root.right
        self.helper(root.left)
        self.helper(right)