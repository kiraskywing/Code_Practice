# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        memo = collections.defaultdict(int)
        self.res = 0
        self.helper(root, memo)
        return self.res
    
    def helper(self, root, memo):
        memo[root.val] += 1
        
        if root.left:
            self.helper(root.left, memo)
        if root.right:
            self.helper(root.right, memo)
        if not root.left and not root.right:
            odd_count = 0
            for times in memo.values():
                odd_count += times % 2 != 0
            if odd_count < 2:
                self.res += 1
        
        memo[root.val] -= 1

class Solution2:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, count):
        if not root:
            return 0
        
        count ^= 1 << (root.val)
        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right and count & (count - 1) == 0:
            res += 1
        return res