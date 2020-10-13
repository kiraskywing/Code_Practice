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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):

        total, size, max_node, max_average = self.helper(root)
        return max_node

    def helper(self, root):
        if not root:
            return 0, 0, None, -sys.maxsize

        left_sum, left_size, left_node, left_max = self.helper(root.left)
        right_sum, right_size, right_node, right_max = self.helper(root.right)

        value = left_sum + right_sum + root.val
        size = left_size + right_size + 1

        if left_max == max(left_max, right_max, value / size):
            return value, size, left_node, left_max
        if right_max == max(left_max, right_max, value / size):
            return value, size, right_node, right_max

        return value, size, root, value / size
