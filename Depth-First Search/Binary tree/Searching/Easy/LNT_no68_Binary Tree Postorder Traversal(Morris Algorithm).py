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

        result = []
        cur = root

        while cur:
            if not cur.right:
                result.append(cur.val)
                cur = cur.left
            else:
                pre = cur.right
                while pre.left and pre.left != cur:
                    pre = pre.left

                if pre.left == cur:
                    pre.left = None
                    cur = cur.left
                else:
                    result.append(cur.val)
                    pre.left = cur
                    cur = cur.right

        return result[::-1]
