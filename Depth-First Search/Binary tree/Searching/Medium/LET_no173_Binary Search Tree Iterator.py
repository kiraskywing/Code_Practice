# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack[-1]
        if cur.right:
            nxt = cur.right
            while nxt:
                self.stack.append(nxt)
                nxt = nxt.left
        else:
            nxt = self.stack.pop()
            while self.stack and self.stack[-1].right == nxt:
                nxt = self.stack.pop()
        return cur.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

class BSTIterator2:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur = self.stack.pop()
        res = cur.val
        if cur.right:
            cur = cur.right
            while cur:
                self.stack.append(cur)
                cur = cur.left
        
        return res

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()