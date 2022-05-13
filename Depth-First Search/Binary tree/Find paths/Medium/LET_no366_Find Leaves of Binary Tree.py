# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        memo = collections.defaultdict(list)
        self.dfs(root, memo)
        return [memo[i] for i in range(1, len(memo) + 1)]
    
    def dfs(self, cur, memo):
        if not cur:
            return 0
        
        left_height = self.dfs(cur.left, memo)
        right_height = self.dfs(cur.right, memo)
        cur_height = max(left_height, right_height) + 1
        memo[cur_height].append(cur.val)
        
        return cur_height