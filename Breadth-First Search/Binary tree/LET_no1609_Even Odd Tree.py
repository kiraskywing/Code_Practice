# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_even = False
        
        while queue:
            pre = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_even:
                    if node.val % 2 != 0: return False
                    if pre and pre.val <= node.val: return False
                else:
                    if node.val % 2 == 0: return False
                    if pre and pre.val >= node.val: return False
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                pre = node
            is_even = not is_even
        
        return True