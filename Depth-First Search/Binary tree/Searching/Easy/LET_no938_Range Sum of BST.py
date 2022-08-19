# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if not root:
            return 0
        
        stack = [root]
        res = 0
        
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                res += node.val
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return res

class Solution2:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.helper(root, low, high)
    
    def helper(self, cur, low, high):
        if not cur:
            return 0
        
        res = 0
        if cur.val < low:
            res += self.helper(cur.right, low, high)
        elif cur.val > high:
            res += self.helper(cur.left, low, high)
        else:
            res += cur.val + self.helper(cur.left, low, high) + self.helper(cur.right, low, high)
        
        return res