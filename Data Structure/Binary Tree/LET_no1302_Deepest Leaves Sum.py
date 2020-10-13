# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        memo = collections.defaultdict(int)
        self.dfs(root, 1, memo)
        return memo[max(memo)]

    def dfs(self, root, level, memo):
        if not root:
            return
        memo[level] += root.val
        self.dfs(root.left, level + 1, memo)
        self.dfs(root.right, level + 1, memo)