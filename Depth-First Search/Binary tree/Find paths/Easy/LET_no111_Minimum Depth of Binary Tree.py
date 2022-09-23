"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """

    def minDepth(self, root: TreeNode) -> int:
        if not root: 
            return 0
        if not root.left and not root.right: 
            return 1
        
        if root.left and not root.right: 
            return 1 + self.minDepth(root.left)
        if root.right and not root.left: 
            return 1 + self.minDepth(root.right)
        
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.res = float('inf')
        self.dfs(root, 1)
        return self.res
    
    def dfs(self, root, depth):
        if not root.left and not root.right:
            self.res = min(self.res, depth)
        if root.left:
            self.dfs(root.left, depth + 1)
        if root.right:
            self.dfs(root.right, depth + 1)

class Solution3:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 1
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        
        return -1

