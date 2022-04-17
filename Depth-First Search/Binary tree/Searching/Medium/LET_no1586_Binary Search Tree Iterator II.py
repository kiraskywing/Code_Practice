# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        dummy = TreeNode(val=-1, right=root)
        self.stack = [dummy]
        
        self.left_most_val, self.right_most_val = 0, 0
        cur = root
        while cur:
            self.left_most_val = cur.val
            cur = cur.left
        cur = root
        while cur:
            self.right_most_val = cur.val
            cur = cur.right

    def hasNext(self) -> bool:
        return self.stack[-1].val < self.right_most_val

    def next(self) -> int:
        node = self.stack[-1]
        if node.right:
            node = node.right
            while node:
                self.stack.append(node)
                node = node.left
            return self.stack[-1].val
        
        node = self.stack.pop()
        while self.stack and self.stack[-1].left is not node:
            node = self.stack.pop()
        return self.stack[-1].val

    def hasPrev(self) -> bool:
        return self.stack[-1].val > self.left_most_val

    def prev(self) -> int:
        node = self.stack[-1]
        if node.left:
            node = node.left
            while node:
                self.stack.append(node)
                node = node.right
            return self.stack[-1].val
        
        node = self.stack.pop()
        while self.stack and self.stack[-1].right is not node:
            node = self.stack.pop()
        return self.stack[-1].val


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.hasNext()
# param_2 = obj.next()
# param_3 = obj.hasPrev()
# param_4 = obj.prev()