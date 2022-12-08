# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        memo1, memo2 = [], []
        self.helper(root1, memo1)
        self.helper(root2, memo2)
        return memo1 == memo2

    def helper(self, cur, memo):
        if not cur:
            return

        if not cur.left and not cur.right:
            memo.append(cur.val)
            return 
        if cur.left:
            self.helper(cur.left, memo)
        if cur.right:
            self.helper(cur.right, memo)