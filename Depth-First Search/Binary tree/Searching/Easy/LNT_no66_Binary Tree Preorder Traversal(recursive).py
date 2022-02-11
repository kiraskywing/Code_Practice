"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        result = []
        self.dfs(root, result)
        return result

    def dfs(self, root, result):
        if not root:
            return

        result.append(root.val)
        self.dfs(root.left, result)
        self.dfs(root.right, result)