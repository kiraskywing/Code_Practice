# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = collections.deque(preorder)
        inorder = {num: i for i, num in enumerate(inorder)}
        return self.getTree(preorder, inorder, 0, len(inorder) - 1)
    
    def getTree(self, preorder, inorder, left, right):
        if left > right:
            return None
        
        root_val = preorder.popleft()
        root = TreeNode(root_val)
        idx = inorder[root_val]
        root.left = self.getTree(preorder, inorder, left, idx - 1)
        root.right = self.getTree(preorder, inorder, idx + 1, right)
        
        return root