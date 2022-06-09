"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """

    def longestConsecutive(self, root):
        return self.dfs(None, root, 0)

    def dfs(self, parent, root, length):
        if not root:
            return length

        if parent and root.val == parent.val + 1:
            length += 1
        else:
            length = 1

        return max(length, max(self.dfs(root, root.left, length), self.dfs(root, root.right, length)))

class Solution2:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        _, res = self.helper(root)
        return res
    
    def helper(self, root):
        if not root:
            return 0, 0
        
        left_in, left_res = self.helper(root.left)
        right_in, right_res = self.helper(root.right)
        cur_in = 1
        
        if root.left and root.left.val - 1 == root.val:
            cur_in = max(cur_in, left_in + 1)
        if root.right and root.right.val - 1 == root.val:
            cur_in = max(cur_in, right_in + 1)
        
        return cur_in, max(cur_in, left_res, right_res)
