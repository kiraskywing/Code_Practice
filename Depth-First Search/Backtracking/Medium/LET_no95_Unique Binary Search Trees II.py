# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.helper(1, n)
    
    def helper(self, first, last):
        res = []
        for i in range(first, last + 1):
            for left in self.helper(first, i - 1):
                for right in self.helper(i + 1, last):
                    node = TreeNode(i)
                    node.left = left
                    node.right = right
                    res.append(node)
        return res or [None]