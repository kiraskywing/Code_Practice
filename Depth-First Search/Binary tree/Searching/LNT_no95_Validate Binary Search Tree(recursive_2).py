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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):

        self.last_val = None
        return self.validate(root)

    def validate(self, root):

        if not root:
            return True

        if not self.validate(root.left):
            return False

        if self.last_val is not None and self.last_val >= root.val:
            return False

        self.last_val = root.val

        if not self.validate(root.right):
            return False

        return True
