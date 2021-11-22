# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if root.val == key:
            if not root.right:
                nxt = root.left
                return nxt
            else:
                nxt = root.right
                while nxt.left:
                    nxt = nxt.left
                root.val, nxt.val = nxt.val, root.val
                root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        
        return root