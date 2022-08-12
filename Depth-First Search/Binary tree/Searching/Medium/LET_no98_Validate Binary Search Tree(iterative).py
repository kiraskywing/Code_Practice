# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        stack = []
        while root:
            stack.append(root)
            root = root.left
            
        prev = None
        while stack:
            cur = stack[-1]
            if prev and prev.val >= cur.val:
                return False
            
            if cur.right:
                nxt = cur.right
                while nxt:
                    stack.append(nxt)
                    nxt = nxt.left
            else:
                node = stack.pop()
                while stack and stack[-1].right is node:
                    node = stack.pop()
                    
            prev = cur
        
        return True