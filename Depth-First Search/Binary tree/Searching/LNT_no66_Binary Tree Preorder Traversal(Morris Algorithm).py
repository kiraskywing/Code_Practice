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
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        if not root:
            return []

        result = []
        cur = root

        while cur:
            if not cur.left:
                result.append(cur.val)
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right

                if pre.right == cur:
                    pre.right = None
                    cur = cur.right
                else:
                    result.append(cur.val)
                    pre.right = cur
                    cur = cur.left

        return result
