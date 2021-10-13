# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        return self.helper(preorder[::-1], float('inf'))
    
    def helper(self, nums, bound):
        if not nums or nums[-1] > bound:
            return None
        
        root = TreeNode(nums.pop())
        root.left = self.helper(nums, root.val)
        root.right = self.helper(nums, bound)
        
        return root