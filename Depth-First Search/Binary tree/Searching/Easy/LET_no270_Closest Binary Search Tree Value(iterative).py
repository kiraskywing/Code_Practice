# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        upper = lower = root
        while root:
            if root.val > target:
                upper = root
                root = root.left
            elif root.val < target:
                lower = root
                root = root.right
            else:
                return root.val
            
        if abs(upper.val - target) < abs(lower.val - target):
            return upper.val
        return lower.val