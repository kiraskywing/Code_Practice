# The same as LeetCode no113. Path Sum II

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
    def binaryTreePathSum(self, root, target):

        self.result = []
        path = []
        self.search(root, 0, target, path)

        return self.result

    def search(self, root, cur, target, path):

        if not root:
            return

        cur += root.val
        path.append(root.val)

        if not root.left and not root.right and cur == target:
            self.result.append(path[:])

        self.search(root.left, cur, target, path)
        self.search(root.right, cur, target, path)

        path.pop()