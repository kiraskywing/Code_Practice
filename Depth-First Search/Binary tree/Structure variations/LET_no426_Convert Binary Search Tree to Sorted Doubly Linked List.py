"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        dummy = Node(-1, None, None)
        prev = dummy
        stack = []
        node = root

        while stack or node is not None:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            prev.right, node.left = node, prev
            prev = node
            node = node.right

        dummy.right.left, prev.right = prev, dummy.right

        return dummy.right

class Solution2:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        left_head = self.treeToDoublyList(root.left)
        right_head = self.treeToDoublyList(root.right)
        root.left = root.right = root
        
        return self.connect(self.connect(left_head, root), right_head)
    
    def connect(self, node1, node2):
        if not node1:
            return node2
        if not node2:
            return node1
        
        tail1, tail2 = node1.left, node2.left
        tail1.right = node2
        node2.left = tail1
        tail2.right = node1
        node1.left = tail2
        
        return node1