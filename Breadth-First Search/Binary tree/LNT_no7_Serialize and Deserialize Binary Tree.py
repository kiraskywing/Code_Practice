"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """

    def serialize(self, root):

        if not root:
            return ""

        q = collections.deque([root])
        bfs_order = []

        while q:
            node = q.popleft()
            bfs_order.append(str(node.val) if node else "#")

            if node:
                q.append(node.left)
                q.append(node.right)

        return " ".join(bfs_order)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    """

    def deserialize(self, data):

        if not data:
            return

        bfs_order = []
        for val in data.split():
            if val != "#":
                bfs_order.append(TreeNode(val))
            else:
                bfs_order.append(None)

        root = bfs_order[0]
        nodes, slow_index, fast_index = [root], 0, 1

        while fast_index < len(bfs_order):
            node = nodes[slow_index]
            node.left = bfs_order[fast_index]
            node.right = bfs_order[fast_index + 1]
            slow_index += 1
            fast_index += 2

            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)

        return root
