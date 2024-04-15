# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, cur, res):
        if not cur:
            return

        if cur.left and not cur.right:
            res.append(cur.left.val)
            
        if cur.right and not cur.left:
            res.append(cur.right.val)
        
        self.helper(cur.left, res)
        self.helper(cur.right, res)