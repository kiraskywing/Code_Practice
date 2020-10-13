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

        is_bst, min_node, max_node = self.validate(root)
        return is_bst

    def validate(self, root):

        if not root:
            return True, None, None

        left_bst, left_min, left_max = self.validate(root.left)
        right_bst, right_min, right_max = self.validate(root.right)

        if not left_bst or not right_bst:
            return False, None, None
        if left_max is not None and left_max >= root.val:
            return False, None, None
        if right_min is not None and right_min <= root.val:
            return False, None, None

        min_node = left_min if left_min is not None else root.val
        max_node = right_max if right_max is not None else root.val

        return True, min_node, max_node
