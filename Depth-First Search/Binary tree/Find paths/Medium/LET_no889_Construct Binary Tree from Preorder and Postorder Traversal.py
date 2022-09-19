class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.i_pre = self.i_post = 0
        return self.helper(preorder, postorder)
    
    def helper(self, preorder, postorder):
        cur = TreeNode(preorder[self.i_pre])
        self.i_pre += 1
        
        if cur.val != postorder[self.i_post]:
            cur.left = self.helper(preorder, postorder)
        if cur.val != postorder[self.i_post]:
            cur.right = self.helper(preorder, postorder)
        self.i_post += 1
        
        return cur