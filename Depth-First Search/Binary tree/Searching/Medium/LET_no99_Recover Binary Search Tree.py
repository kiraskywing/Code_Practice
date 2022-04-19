# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev_node = TreeNode(float('-inf'))
        self.first_node, self.second_node = None, None
        self.dfs(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
        
    def dfs(self, root):
        if not root:
            return
        
        self.dfs(root.left)
        if not self.first_node and self.prev_node.val >= root.val:
            self.first_node = self.prev_node
        if self.first_node and self.prev_node.val >= root.val:
            self.second_node = root
        self.prev_node = root
        self.dfs(root.right)