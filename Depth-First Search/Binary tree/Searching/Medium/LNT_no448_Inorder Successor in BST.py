# The same as LeetCode no285. Inorder Successor in BST

"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """

    def inorderSuccessor(self, root, p):
        ans = None

        while root:
            if root.val <= p.val:
                root = root.right
            else:
                ans = root
                root = root.left

        return ans
