# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        self.res = 0
        self.helper(root, distance)
        return self.res

    def helper(self, cur, distance):
        if not cur:
            return []
        if not cur.left and not cur.right:
            return [1]

        left_list = self.helper(cur.left, distance)
        right_list = self.helper(cur.right, distance)
        for left in left_list:
            for right in right_list:
                self.res += left + right <= distance

        return [depth + 1 for depth in left_list + right_list if depth + 1 < distance]