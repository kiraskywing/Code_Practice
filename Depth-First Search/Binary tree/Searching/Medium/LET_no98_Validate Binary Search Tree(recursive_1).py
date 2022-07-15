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
    @return: True if the binary tree is BST, or false
    """

    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, cur, min_val, max_val):
        if not cur:
            return True
        
        if not (min_val < cur.val < max_val):
            return False
        return self.helper(cur.left, min_val, cur.val) and self.helper(cur.right, cur.val, max_val)