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
        left = right = 0
        while queue:
            for _ in range(len(queue)):
                node, idx = queue.popleft()
                left = min(left, idx)
                right = max(right, idx)
                memo[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx - 1))
                if node.right:
                    queue.append((node.right, idx + 1))
        
        return [memo[idx] for idx in range(left, right + 1)]

"""
traverse a given binary tree from top to bottom, column by column.
The same row and column: from left to right

example 1:
    3
   / \
  9   20
     /  \
    15   7
Output: [[9],[3,15],[20],[7]]

example 2:
        3
       / \
      /   \
     9     8
    / \   / \
   4  0  1   7
Output: [[4],[9],[3,0,1],[8],[7]]

"""