# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
    
    def helper(self, root, p, q):
        if not root:
            return None
        if root is p or root is q:
            return root
        
        leftRes = self.helper(root.left, p, q)
        rightRes = self.helper(root.right, p, q)
        if leftRes and rightRes:
            return root
        if leftRes:
            return leftRes
        if rightRes:
            return rightRes
        return None