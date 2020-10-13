"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {int} an integer
    def leafSum(self, root):

        self.ans = 0
        self.dfs(root)

        return self.ans

    def dfs(self, root):

        if not root:
            return

        if not root.left and not root.right:
            self.ans += root.val

        self.dfs(root.left)
        self.dfs(root.right)