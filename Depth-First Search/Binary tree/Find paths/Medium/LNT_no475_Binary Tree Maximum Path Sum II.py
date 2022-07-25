"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the root of binary tree.
    @return: An integer
    """

    def maxPathSum2(self, root):
        if not root:
            return -sys.maxsize

        return max(0, self.maxPathSum2(root.left), self.maxPathSum2(root.right)) + root.val

class Solution2:
    """
    @param root: the root of binary tree.
    @return: An integer
    """
    def max_path_sum2(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        res = float('-inf')
        cur = 0
        stack = []
        while root:
            stack.append(root)
            cur += root.val
            res = max(res, cur)
            root = root.left

        while stack:
            node = stack[-1]
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    cur += node.val
                    res = max(res, cur)
                    node = node.left
            else:
                node = stack.pop()
                cur -= node.val
                while stack and stack[-1].right is node:
                    node = stack.pop()
                    cur -= node.val
        
        return res