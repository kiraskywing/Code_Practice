# The same as LeetCode no103. Binary Tree Zigzag Level Order Traversal

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
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):

        if not root:
            return []

        result = []
        queue = collections.deque([root])
        reverse = False

        while queue:
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if reverse:
                result.append(temp[::-1])
            else:
                result.append(temp)
            reverse = not reverse

        return result
