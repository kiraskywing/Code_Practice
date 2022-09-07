# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = []
        self.dfs(root, res)
        return ''.join(res)
    
    def dfs(self, cur, res):
        if not cur:
            return
        
        res.append(str(cur.val))
        if not cur.left and not cur.right:
            return
        
        res.append('(')
        self.dfs(cur.left, res)
        res.append(")")
        
        if cur.right:
            res.append('(')
            self.dfs(cur.right, res)
            res.append(')')