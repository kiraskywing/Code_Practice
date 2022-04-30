from lintcode import (
    TreeNode,
)

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
    @return: the maximum weight node
    """
    def find_subtree(self, root: TreeNode) -> TreeNode:
        _, _, res = self.helper(root)
        return res

    def helper(self, cur):
        if not cur:
            return 0, float('-inf'), None

        left_sum, left_max, left_res = self.helper(cur.left)
        right_sum, right_max, right_res = self.helper(cur.right)
        cur_total = cur.val + left_sum + right_sum
        max_sum = max(left_max, right_max, cur_total)

        if max_sum == cur_total:
            return cur_total, cur_total, cur
        if max_sum == left_max:
            return cur_total, left_max, left_res
        if max_sum == right_max:
            return cur_total, right_max, right_res
