# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        res = []
        return res if self.dfs(root, voyage, res) else [-1]
    
    def dfs(self, node, voyage, res):
        if not node: return True
        if node.val != voyage[self.i]: return False
        self.i += 1
        if node.left and node.left.val != voyage[self.i]:
            res.append(node.val)
            return self.dfs(node.right, voyage, res) and self.dfs(node.left, voyage, res)
        return self.dfs(node.left, voyage, res) and self.dfs(node.right, voyage, res)