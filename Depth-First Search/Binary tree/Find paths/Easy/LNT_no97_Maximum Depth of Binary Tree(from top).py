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
    @return: An integer
    """
    def maxDepth(self, root):

        if not root:
            return 0

        self.result = 1
        self.count(root, 1)
        return self.result

    def count(self, root, height):
        if not root:
            return

        self.result = max(self.result, height)

        self.count(root.left, height + 1)
        self.count(root.right, height + 1)