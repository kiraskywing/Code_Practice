# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        result = []
        self.dfs(root, 0, result)
        return sum(result)
    
    def dfs(self, root, cur, result):
        if not root:
            return
        
        cur = cur * 2 + root.val
        if not root.left and not root.right:
            result.append(cur)
        
        self.dfs(root.left, cur, result)
        self.dfs(root.right, cur, result)
        