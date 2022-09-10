# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([root])
        while queue:
            for _ in range(len(queue)):
                root = queue.popleft()
                if root.right:
                    queue.append(root.right)
                if root.left:
                    queue.append(root.left)
        
        return root.val