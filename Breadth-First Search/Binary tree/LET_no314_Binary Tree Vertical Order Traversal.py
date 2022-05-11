# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        memo = collections.defaultdict(list)
        queue = collections.deque([(root, 0)])
        
        while queue:
            cur, index = queue.popleft()
            memo[index].append(cur.val)
            if cur.left:
                queue.append((cur.left, index - 1))
            if cur.right:
                queue.append((cur.right, index + 1))
        
        return [memo[i] for i in sorted(memo)]