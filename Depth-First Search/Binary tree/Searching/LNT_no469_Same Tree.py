"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):

        if not a and not b:
            return True

        elif not a and b or a and not b:
            return False

        elif a.val != b.val:
            return False

        return self.isIdentical(a.left, b.left) and self.isIdentical(a.right, b.right)