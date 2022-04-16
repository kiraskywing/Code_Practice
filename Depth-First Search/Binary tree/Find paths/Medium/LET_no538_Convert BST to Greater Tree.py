
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.cur_sum = 0
        self.helper(root)
        return root
    
    def helper(self, root):
        if not root:
            return 
        
        self.helper(root.right)
        root.val += self.cur_sum
        self.cur_sum = root.val
        self.helper(root.left)