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
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):

        if not root:
            return []

        prev = None
        res = []

        stack = [root]

        while stack:
            cur = stack[-1]
            if not prev or prev.left == cur or prev.right == cur:
                if cur.left:
                    stack.append(cur.left)
                elif cur.right:
                    stack.append(cur.right)

            elif cur.left == prev:
                if cur.right:
                    stack.append(cur.right)

            else:
                res.append(stack[-1].val)
                stack.pop()

            prev = cur

        return res