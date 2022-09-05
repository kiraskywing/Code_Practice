# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.helper(root, 0)
    
    def helper(self, cur, num):
        num = num * 10 + cur.val
        if not cur.left and not cur.right:
            return num
        elif not cur.left:
            return self.helper(cur.right, num)
        elif not cur.right:
            return self.helper(cur.left, num)
        return self.helper(cur.left, num) + self.helper(cur.right, num)


class Solution2:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = [(root, 0)]
        
        while stack:
            node, val = stack.pop()
            val = val * 10 +  node.val
            if not node.left and not node.right:
                res += val
            if node.left:
                stack.append((node.left, val))
            if node.right:
                stack.append((node.right, val))
        
        return res