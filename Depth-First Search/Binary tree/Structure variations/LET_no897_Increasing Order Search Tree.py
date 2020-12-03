# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.helper(root, None)
    
    def helper(self, root, tail):
        if not root:
            return tail
        
        res = self.helper(root.left, root)
        root.left = None
        root.right = self.helper(root.right, tail)
        
        return res