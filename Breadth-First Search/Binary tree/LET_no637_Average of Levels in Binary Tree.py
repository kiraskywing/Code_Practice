# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = collections.deque([root])
        val = root.val
        res = []
        
        while queue:
            res.append(val / len(queue))
            val = 0
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    val += cur.left.val
                    queue.append(cur.left)
                if cur.right:
                    val += cur.right.val
                    queue.append(cur.right)
        
        return res