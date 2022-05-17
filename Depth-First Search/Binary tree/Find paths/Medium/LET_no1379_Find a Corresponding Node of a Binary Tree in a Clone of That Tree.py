# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        return self.helper(original, cloned, target)
    
    def helper(self, original, cloned, target):
        if not original:
            return
        
        if original == target:
            return cloned
        
        return self.helper(original.left, cloned.left, target) or self.helper(original.right, cloned.right, target)