# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        res, _ = self.helper(s, 0)
        return res
    
    def helper(self, s, i):
        start = i
        while i < len(s) and s[i] not in "()":
            i += 1
        root = TreeNode(int(s[start:i]))
        
        if i < len(s) and s[i] == '(':
            root.left, i = self.helper(s, i + 1)
        if i < len(s) and s[i] == '(':
            root.right, i = self.helper(s, i + 1)
        
        return root, i + 1