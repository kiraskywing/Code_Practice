# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder = {val:i for i, val in enumerate(inorder)}
        self.cur_p = 0
        return self.helper(preorder, inorder, 0, len(inorder) - 1)
    
    def helper(self, preorder, inorder, left_i, right_i):
        if left_i > right_i:
            return None
        
        cur_node = TreeNode(preorder[self.cur_p])
        self.cur_p += 1
        
        cur_i = inorder[cur_node.val]
        cur_node.left = self.helper(preorder, inorder, left_i, cur_i - 1)
        cur_node.right = self.helper(preorder, inorder, cur_i + 1, right_i)
        return cur_node