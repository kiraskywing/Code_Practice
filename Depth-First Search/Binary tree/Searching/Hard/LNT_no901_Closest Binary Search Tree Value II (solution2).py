# The same as LeetCode no272. Closest Binary Search Tree Value II

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        if not root or k == 0:
            return []
        
        lowers = self.getStack(root, target)
        uppers = lowers[:]
        if lowers[-1].val < target:
            self.moveUpper(uppers)
        else:
            self.moveLower(lowers)
            
        res = []
        for _ in range(k):
            if self.isLower(lowers, uppers, target):
                res.append(lowers[-1].val)
                self.moveLower(lowers)
            else:
                res.append(uppers[-1].val)
                self.moveUpper(uppers)
        return res
    
    def getStack(self, root, target):
        res = []
        while root:
            res.append(root)
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res
    
    def moveUpper(self, stack):
        cur = stack[-1]
        if cur.right:
            cur = cur.right
            while cur:
                stack.append(cur)
                cur = cur.left
        else:
            stack.pop()
            while stack and stack[-1].right == cur:
                cur = stack.pop()
    
    def moveLower(self, stack):
        cur = stack[-1]
        if cur.left:
            cur = cur.left
            while cur:
                stack.append(cur)
                cur = cur.right
        else:
            stack.pop()
            while stack and stack[-1].left == cur:
                cur = stack.pop()
    
    def isLower(self, lowers, uppers, target):
        if not uppers:
            return True
        if not lowers:
            return False
        
        return target - lowers[-1].val < uppers[-1].val - target