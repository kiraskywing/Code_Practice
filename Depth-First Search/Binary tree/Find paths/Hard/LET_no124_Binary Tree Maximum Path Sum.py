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
    def maxPathSum(self, root):

        maxSum, _ = self.dfs(root)
        return maxSum

    def dfs(self, root):
        if not root:
            return -sys.maxsize, 0

        left_max, left_sum = self.dfs(root.left)
        right_max, right_sum = self.dfs(root.right)
        maxSum = max(left_max, right_max, left_sum + root.val + right_sum)
        singleSum = max(left_sum + root.val, right_sum + root.val, 0)

        return maxSum, singleSum
