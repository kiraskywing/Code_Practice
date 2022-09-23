# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # empty input? => yes, just return false
        
        # Approach: recursive DFS
        # use a helper function pass node, total sum from root, and the targetSum
        # => helper(root, cur_sum, target)
        # case1: no children => return whether cur_sum is equal to target
        # case2: has left child or right child
        #        create a variable res as False
        #        if left child exist => update res = res or the result from left subtree
        #        if right child exist => update res = res or the result from right subtree
        #        => return res
        
        if not root:
            return False
        
        return self.helper(root, 0, targetSum)   # Time: O(n), Space: O(h) where h is the tree's height
    
    def helper(self, root, cur_sum, target):
        cur_sum += root.val
        
        if not root.left and not root.right:
            return cur_sum == target
        
        res = False
        if root.left:
            res |= self.helper(root.left, cur_sum, target)
        if root.right:
            res |= self.helper(root.right, cur_sum, target)
        return res