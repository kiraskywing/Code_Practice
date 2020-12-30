# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution1:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        self.res = 0
        self.dfs([], root)
        return self.res
    
    def dfs(self, temp, root):
        temp.append(root.val)
        if root.left:
            self.dfs(temp, root.left)
        if root.right:
            self.dfs(temp, root.right)
        if not root.left and not root.right:
            odd = 0
            for key, value in collections.Counter(temp).items():
                if value % 2 != 0:
                    odd += 1
            if odd <= 1:
                self.res += 1
        temp.pop()

class Solution2:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        return self.dfs(root, 0)
        
    def dfs(self, root, count):
        if not root:
            return 0
        
        count ^= 1 << (root.val - 1)
        res = self.dfs(root.left, count) + self.dfs(root.right, count)
        if not root.left and not root.right and count & (count - 1) == 0:
            res += 1
        return res