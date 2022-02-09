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
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):

        minimum, min_subtree, total_sum = self.helper(root)
        return min_subtree

    def helper(self, root):

        if not root:
            return sys.maxsize, None, 0

        left_min, left_subtree, left_sum = self.helper(root.left)
        right_min, right_subtree, right_sum = self.helper(root.right)

        total_sum = left_sum + root.val + right_sum

        if left_min < right_min and left_min < total_sum:
            return left_min, left_subtree, total_sum

        if right_min < left_min and right_min < total_sum:
            return right_min, right_subtree, total_sum

        return total_sum, root, total_sum