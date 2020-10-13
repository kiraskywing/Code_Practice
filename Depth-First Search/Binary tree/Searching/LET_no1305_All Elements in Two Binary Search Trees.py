# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        arr1 = self.inorder(root1)
        arr2 = self.inorder(root2)
        return self.merge_sort(arr1, arr2)
        
    def inorder(self, root):
        if not root:
            return []
        
        dummy = TreeNode()
        dummy.right = root
        stack = [dummy]
        res = []
        
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            
            if stack:
                res.append(stack[-1].val)
        
        return res
    
    def merge_sort(self, arr1, arr2):
        res = []
        i, j = 0, 0
        
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1
        
        if i < len(arr1):
            res.extend(arr1[i:])
        if j < len(arr2):
            res.extend(arr2[j:])
        
        return res