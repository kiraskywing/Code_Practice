# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # empty input? => yes
        
        # Approach: iterative DFS
        # visit left child -> visit right child -> visit root
        # step1: keep pushing child into stack (choose left if left exists, otherwise choose right)
        # step2: pop one node from stack, put node.val into output
        # step3: if current node is left child -> find right child
        #        if right child exists -> repeat step1
        # step4: back to step2 until stack is empty
        
        if not root:
            return []
        
        stack = []    # Space: O(h) where h is the tree's height
        while root:
            stack.append(root)
            if root.left:
                root = root.left
            else:
                root = root.right
            
        res = []
        while stack:    # Time: O(n)
            cur = stack.pop()
            res.append(cur.val)
            if stack and stack[-1].left is cur:
                cur = cur.right
                while cur:
                    stack.append(cur)
                    if cur.left:
                        cur = cur.left
                    else:
                        cur = cur.right
        
        return res