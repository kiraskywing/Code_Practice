"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        max_len, _, _ = self.helper(root)
        return max_len

    def helper(self, root):
        if not root:
            return 0, 0, 0

        max_len, up, down = 0, 0, 0
        for child in root.children:
            c_len, c_up, c_down = self.helper(child)
            max_len = max(max_len, c_len)
            if child.val + 1 == root.val:
                up = max(up, c_up + 1)
            if child.val == root.val + 1:
                down = max(down, c_down + 1)

        max_len = max(max_len, up + 1 + down)
        return max_len, up, down