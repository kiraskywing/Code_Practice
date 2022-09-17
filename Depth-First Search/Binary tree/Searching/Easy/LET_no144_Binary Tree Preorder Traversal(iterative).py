# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # empty input? => yes
        
        # Approach: iterative DFS
        # visit root -> visit left child -> visit right child
        # step1: keep pushing left child into stack, meanwhile put the node.val into output
        # step2: pop node from stack 
        # step3: visit node.right if right child exists, then repeat step1
        #        if right child not exists, repeat step2 -> step3
        
        if not root:
            return []
        
        stack = []
        res = []
        while root:    # Space: O(h) where h is the tree's height
            res.append(root.val)
            stack.append(root)
            root = root.left
            
        while stack:    # Time: O(n)
            cur = stack.pop()
            if cur.right:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    res.append(cur.val)
                    cur = cur.left
        
        return res