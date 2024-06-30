# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        res = [None, None]
        if not root:
            return res

        if root.val > target:
            res[1] = root
            sub_res = self.splitBST(root.left, target)
            root.left = sub_res[1]
            res[0] = sub_res[0]
        else:
            res[0] = root
            sub_res = self.splitBST(root.right, target)
            root.right = sub_res[0]
            res[1] = sub_res[1]            

        return res