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
    @return: true if they are tweaked identical, or false.
    """
    def isTweakedIdentical(self, a, b):

        if not a and not b:
            return True

        if a and b and a.val == b.val:
            return self.isTweakedIdentical(a.left, b.left) and self.isTweakedIdentical(a.right, b.right) or \
                   self.isTweakedIdentical(a.left, b.right) and self.isTweakedIdentical(a.right, b.left)

        return False