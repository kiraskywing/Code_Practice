# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.helper(root, 0)
        return root
    
    def helper(self, root, pre_max):
        if not root:
            return 0
        
        cur_max = root.val + self.helper(root.right, pre_max)
        root.val = cur_max + pre_max
        cur_max += self.helper(root.left, root.val)
        
        return cur_max