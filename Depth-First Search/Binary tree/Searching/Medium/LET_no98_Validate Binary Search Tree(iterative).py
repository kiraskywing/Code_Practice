# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        prev = None
        while stack:
            cur = stack.pop()
            if prev and prev.val >= cur.val:
                return False
            prev = cur
            
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
        
        return True