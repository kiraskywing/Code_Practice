# The same as LeetCode no549. Binary Tree Longest Consecutive Sequence II

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
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive2(self, root):

        max_length, _, _ = self.traverse(root)
        return max_length

    def traverse(self, root):

        if not root:
            return 0, 0, 0

        left_len, left_up, left_down = self.traverse(root.left)
        right_len, right_up, right_down = self.traverse(root.right)

        up, down = 1, 1

        if root.left and root.val - root.left.val == 1:
            up = max(up, left_up + 1)
        if root.left and root.left.val - root.val == 1:
            down = max(down, left_down + 1)

        if root.right and root.val - root.right.val == 1:
            up = max(up, right_up + 1)
        if root.right and root.right.val - root.val == 1:
            down = max(down, right_down + 1)

        length = up + down - 1
        length = max(length, left_len, right_len)

        return length, up, down