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
    @param t1: the root of the first tree
    @param t2: the root of the second tree
    @return: the new binary tree after merge
    """
    def merge_trees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif not t1:
            return t2
        elif not t2:
            return t1
        self.helper(t1, t2)
        return t1
    
    def helper(self, t1, t2):
        t1.val += t2.val
        if t1.left and t2.left:
            self.helper(t1.left, t2.left)
        elif not t1.left:
            t1.left = t2.left
        if t1.right and t2.right:
            self.helper(t1.right, t2.right)
        elif not t1.right:
            t1.right = t2.right
