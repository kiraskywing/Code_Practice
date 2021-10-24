# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res, h = 0, self.getHeight(root)
        while root:
            if self.getHeight(root.right) == h - 1:
                res += 1 << h
                root = root.right
            else:
                res += 1 << (h - 1)
                root = root.left
            h -= 1
        return res
    
    def getHeight(self, root):
        return -1 if not root else 1 + self.getHeight(root.left)