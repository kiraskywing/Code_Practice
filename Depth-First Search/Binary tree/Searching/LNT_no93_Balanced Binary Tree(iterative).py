"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """
    def isBalanced(self, root):

        stack, depth = [], collections.defaultdict(int)

        while root or stack:
            if root:
                stack.append(root)
                root = root.left if root.left else root.right

            else:
                root = stack.pop()
                if abs(depth[root.left] - depth[root.right]) > 1:
                    return False

                depth[root] = 1 + max(depth[root.left], depth[root.right])

                if stack and stack[-1].left == root:
                    root = stack[-1].right
                else:
                    root = None

        return True
