"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):

        if not root:
            return []

        dummy = TreeNode(0)
        dummy.right = root
        stack = [dummy]
        res = []

        while stack:
            node = stack.pop()

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                res.append(stack[-1].val)

        return res