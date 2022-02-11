# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        res, _, _ = self.helper(root)
        return res
    
    def helper(self, root):
        if not root:
            return 0, 0, 0
        
        leftRes, leftSum, leftCount = self.helper(root.left)
        rightRes, rightSum, rightCount = self.helper(root.right)
        
        curSum = leftSum + rightSum + root.val
        curCount = leftCount + rightCount + 1
        curRes = curSum / curCount
        
        return max(leftRes, rightRes, curRes), curSum, curCount