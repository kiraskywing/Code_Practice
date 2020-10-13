"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):

        if not root:
            return 0
        self.length_max = 1
        self.traverse(root, 1)

        return self.length_max

    def traverse(self, root, length):

        if root.left:
            if root.left.val - root.val == 1:
                self.traverse(root.left, length + 1)
            else:
                self.traverse(root.left, 1)

        if root.right:
            if root.right.val - root.val == 1:
                self.traverse(root.right, length + 1)
            else:
                self.traverse(root.right, 1)

        self.length_max = max(self.length_max, length)