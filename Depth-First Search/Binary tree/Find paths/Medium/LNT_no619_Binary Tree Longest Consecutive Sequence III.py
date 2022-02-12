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
        res, _, _ = self.helper(root)
        return res

    def helper(self, root):
        if not root:
            return 0, 0, 0

        res, up, down = 1, 1, 1
        for child in root.children:
            cRes, cUp, cDown = self.helper(child)
            if child and child.val == root.val + 1:
                up = max(up, cUp + 1)
            if child and child.val == root.val - 1:
                down = max(down, cDown + 1)
            res = max(res, up + down - 1, cRes)

        return res, up, down