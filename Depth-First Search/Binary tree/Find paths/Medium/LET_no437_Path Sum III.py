# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        record = collections.defaultdict(int)
        record[0] = 1
        self.res = 0
        self.helper(root, targetSum, record, 0)
        return self.res
    
    def helper(self, root, targetSum, record, preSum):
        if not root:
            return
        
        preSum += root.val
        self.res += record[preSum - targetSum]
        
        record[preSum] += 1
        self.helper(root.left, targetSum, record, preSum)
        self.helper(root.right, targetSum, record, preSum)
        record[preSum] -= 1