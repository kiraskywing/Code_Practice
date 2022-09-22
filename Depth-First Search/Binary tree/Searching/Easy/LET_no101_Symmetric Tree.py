# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Approach: recursive DFS
        # initialize two nodes as root, send to a helper function
        # if one traverse to its left subtree, the other one should traverse its right subtree
        # compare whether the values of the two nodes are the same
        # do above steps recursively
        
        return self.helper(root, root)
    
    def helper(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None or node1.val != node2.val:
            return False
        
        return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)