# The same as LeetCode no257. Binary Tree Paths

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):

        if not root:
            return []

        result = []
        self.dfs(root, [str(root.val)], result)
        return result

    def dfs(self, root, path, result):

        if not root.left and not root.right:
            result.append("->".join(path))
            return

        if root.left:
            path.append(str(root.left.val))
            self.dfs(root.left, path, result)
            path.pop()

        if root.right:
            path.append(str(root.right.val))
            self.dfs(root.right, path, result)
            path.pop()

        return