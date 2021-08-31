"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param nums: an array
    @return: the maximum tree
    """
    def constructMaximumBinaryTree(self, nums):
        # Write your code here
        return self.helper(nums, 0, len(nums) - 1)
    
    def helper(self, nums, left, right):
        if left > right:
            return None
        
        index, value = left, nums[left]
        for i in range(left, right + 1):
            if nums[i] > value:
                index, value = i, nums[i]
        
        node = TreeNode(value)
        node.left = self.helper(nums, left, index - 1)
        node.right = self.helper(nums, index + 1, right)

        return node
