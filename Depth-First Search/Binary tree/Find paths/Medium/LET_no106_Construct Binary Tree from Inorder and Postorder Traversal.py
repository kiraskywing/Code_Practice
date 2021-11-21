# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        table = {val:i for i, val in enumerate(inorder)}
        
        def helper(i_left, i_right):
            if i_left > i_right:
                return None
            
            cur = TreeNode(postorder.pop())
            mid = table[cur.val]
            cur.right = helper(mid + 1, i_right)
            cur.left = helper(i_left, mid - 1)
            return cur
        
        return helper(0, len(inorder) - 1)