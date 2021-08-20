# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        record = set()
        total = self.subTreeSum(root, record)
        res = 0
        for sub in record:
            res = max(res, (total - sub) * sub)
        return res % (10 ** 9 + 7)
    
    def subTreeSum(self, root, record):
        if not root:
            return 0
        
        sub = root.val + self.subTreeSum(root.left, record) + self.subTreeSum(root.right, record)
        record.add(sub)
        return sub