from typing import (
    List,
)
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
    @param a: Given an integer array with no duplicates.
    @return: The root of max tree.
    """
    def max_tree(self, a: List[int]) -> TreeNode:
        stack = []
        for num in a:
            cur = TreeNode(num)
            while stack and stack[-1].val < num:
                cur.left = stack.pop()
            if stack:
                stack[-1].right = cur
            stack.append(cur)
        
        return stack[0]
