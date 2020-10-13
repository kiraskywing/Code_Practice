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

    def longestConsecutive(self, root):
        return self.dfs(None, root, 0)

    def dfs(self, parent, root, length):
        if not root:
            return length

        if parent and root.val == parent.val + 1:
            length += 1
        else:
            length = 1

        return max(length, max(self.dfs(root, root.left, length), self.dfs(root, root.right, length)))
