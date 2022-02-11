# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        res, stack, cur = [], [], root
        while cur:
            stack.append(cur)
            if cur.left:
                cur = cur.left
            else:
                cur = cur.right
        
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if stack and stack[-1].left == cur:
                cur = stack[-1].right
                while cur:
                    stack.append(cur)
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right
        
        return res