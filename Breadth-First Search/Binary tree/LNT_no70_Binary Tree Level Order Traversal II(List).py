"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """

    def levelOrderBottom(self, root):

        if not root:
            return []

        result = []
        q = [root]

        while q:
            temp = []
            result.append([node.val for node in q])

            for node in q:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

            q = temp

        return result[::-1]
