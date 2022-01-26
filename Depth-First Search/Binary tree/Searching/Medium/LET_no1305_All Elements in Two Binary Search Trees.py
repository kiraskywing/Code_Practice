# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        s1, s2 = [], []
        self.postOrder(root1, s1)
        self.postOrder(root2, s2)
        return self.merge(s1, s2)
    
    def postOrder(self, cur, s):
        if not cur:
            return
        
        self.postOrder(cur.left, s)
        s.append(cur.val)
        self.postOrder(cur.right, s)
        
    def merge(self, s1, s2):
        m, n = len(s1), len(s2)
        i, j = 0, 0
        res = []
        
        while i < m and j < n:
            if s1[i] < s2[j]:
                res.append(s1[i])
                i += 1
            else:
                res.append(s2[j])
                j += 1
        
        res.extend(s1[i:])
        res.extend(s2[j:])
        
        return res