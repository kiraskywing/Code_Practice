# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node):
            if not node: return "coverd"

            left, right = dfs(node.left), dfs(node.right)
            if left == "toBeCovered" or right == "toBeCovered":
                self.res += 1
                return "covering"
            return "covered" if left == "covering" or right == "covering" else "toBeCovered"
    
        return (dfs(root) == "toBeCovered") + self.res
    
    