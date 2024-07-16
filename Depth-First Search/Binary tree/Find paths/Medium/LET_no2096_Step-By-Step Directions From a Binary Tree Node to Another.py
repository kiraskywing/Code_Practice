# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        path_to_start, path_to_dest = [], []
        self.helper(root, startValue, path_to_start)
        self.helper(root, destValue, path_to_dest)
        
        while path_to_start and path_to_dest and path_to_start[-1] == path_to_dest[-1]:
            path_to_start.pop()
            path_to_dest.pop()
        
        return 'U' * len(path_to_start) + ''.join(c for c in reversed(path_to_dest))

    def helper(self, cur, target, path):
        if cur.val == target:
            return True
        if cur.left and self.helper(cur.left, target, path):
            path.append('L')
        elif cur.right and self.helper(cur.right, target, path):
            path.append('R')
        return len(path) > 0