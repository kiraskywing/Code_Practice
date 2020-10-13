"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """

    def lowestCommonAncestor(self, root, A, B):
        if not root:
            return None

        if root == A or root == B:
            return root

        left_find = self.lowestCommonAncestor(root.left, A, B)
        right_find = self.lowestCommonAncestor(root.right, A, B)

        if left_find and right_find:
            return root
        if left_find:
            return left_find
        if right_find:
            return right_find
        return None
