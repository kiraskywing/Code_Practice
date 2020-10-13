"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """

    def rightSideView(self, root):

        self.result = []
        self.maxlevel = 1

        self.traverse(root, 1)
        return self.result

    def traverse(self, root, level):
        if not root:
            return

        if level > self.maxlevel or level == 1:
            self.result.append(root.val)
            self.maxlevel = level

        self.traverse(root.right, level + 1)
        self.traverse(root.left, level + 1)