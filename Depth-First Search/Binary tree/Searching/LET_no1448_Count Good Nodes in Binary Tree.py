# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, float('-inf'))
    
    def dfs(self, root, maxNum):
        if not root:
            return 0
        
        maxNum = max(maxNum, root.val)
        res = 1 if root.val >= maxNum else 0
        res += self.dfs(root.left, maxNum) + self.dfs(root.right, maxNum)
        
        return res