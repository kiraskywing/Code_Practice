# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, 0)
        return self.res
    
    def dfs(self, root, cur):
        if not root:
            return
        
        cur = cur * 10 + root.val
        if not root.left and not root.right:
            self.res += cur
        self.dfs(root.left, cur)
        self.dfs(root.right, cur)