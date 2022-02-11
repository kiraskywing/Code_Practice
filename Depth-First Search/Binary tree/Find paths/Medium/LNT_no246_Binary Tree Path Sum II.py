"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """

    def binaryTreePathSum2(self, root, target):
        if not root:
            return []
        path, result = [], []
        self.dfs(root, path, 0, target, result)
        return result

    def dfs(self, root, path, count, target, result):
        if not root:
            return

        path.append(root.val)
        value = target
        for i in range(count, -1, -1):
            value -= path[i]
            if value == 0:
                result.append(path[i:])

        self.dfs(root.left, path, count + 1, target, result)
        self.dfs(root.right, path, count + 1, target, result)

        path.pop()