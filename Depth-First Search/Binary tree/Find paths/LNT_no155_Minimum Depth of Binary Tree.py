# The same as Leetcode no111. Minimum Depth of Binary Tree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        
        if root.left and not root.right: return 1 + self.minDepth(root.left)
        if root.right and not root.left: return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))



