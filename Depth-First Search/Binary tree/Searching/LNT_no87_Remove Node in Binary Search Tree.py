"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):

        if not root:
            return root

        if value < root.val:
            root.left = self.removeNode(root.left, value)
        elif value > root.val:
            root.right = self.removeNode(root.right, value)
        else:
            if root.left and root.right:
                new_node = self.find_max(root)
                root.val = new_node.val
                root.left = self.removeNode(root.left, new_node.val)
            elif not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                root = None

        return root

    def find_max(self, root):

        root = root.left

        while root.right:
            root = root.right

        return root