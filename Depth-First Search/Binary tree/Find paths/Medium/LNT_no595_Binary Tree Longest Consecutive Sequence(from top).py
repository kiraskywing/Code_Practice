# The same as LeetCode no298. Binary Tree Longest Consecutive Sequence

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
        self.res = 1
        self.helper(root, None, 1)
        return self.res
    
    def helper(self, cur, pre, count):
        if not cur:
            return
        
        if pre and cur.val == pre.val + 1:
            count += 1
            self.res = max(self.res, count)
        else:
            count = 1
            
        self.helper(cur.left, cur, count)
        self.helper(cur.right, cur, count)