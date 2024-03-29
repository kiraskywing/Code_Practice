# The same as LeetCode no226. Invert Binary Tree

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

    def invertBinaryTree(self, root):
        if not root:
            return

        root.left, root.right = root.right, root.left

        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

        return root