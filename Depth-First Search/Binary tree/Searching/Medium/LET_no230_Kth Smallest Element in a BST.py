# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        while root:
            stack.append(root)
            root = root.left
        
        for _ in range(k - 1):
            cur = stack[-1]
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    cur = cur.left
            else:
                cur = stack.pop()
                while stack and stack[-1].right is cur:
                    cur = stack.pop()
        
        return stack[-1].val