# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = collections.deque([])
        if root:
            queue.append(root)
        res = []
        
        while queue:
            n = len(queue)
            res.append(queue[-1].val)
            for i in range(n):
                cur = queue.popleft()
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
        
        return res
    
class Solution2:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.max_level = 1
        res = []
        self.helper(root, 1, res)
        return res

    def helper(self, root, level, res):
        if not root:
            return

        if level > self.max_level or level == 1:
            res.append(root.val)
            self.max_level = level

        self.helper(root.right, level + 1, res)
        self.helper(root.left, level + 1, res)