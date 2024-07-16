# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        if p is q:
            return 0
        
        self.res = 0
        self.helper(root, p, q)
        return self.res

    def helper(self, cur, p, q):
        if not cur:
            return -1

        left_count = self.helper(cur.left, p, q)
        right_count = self.helper(cur.right, p, q)

        if cur.val == p or cur.val == q:
            if left_count < 0 and right_count < 0:
                return 0
            
            self.res = 1 + max(left_count, right_count)
            return -1
        
        if left_count >= 0 and right_count >= 0:
            self.res = 2 + left_count + right_count
            return -1

        if left_count >= 0:
            return left_count + 1
        if right_count >= 0:
            return right_count + 1
        
        return -1
