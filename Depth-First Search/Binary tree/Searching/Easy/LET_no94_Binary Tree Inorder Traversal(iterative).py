# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res, stack, cur = [], [], root
        while cur:
            stack.append(cur)
            cur = cur.left
            
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        return res
        