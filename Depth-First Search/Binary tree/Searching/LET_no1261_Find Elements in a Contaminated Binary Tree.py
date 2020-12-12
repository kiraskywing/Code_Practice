# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:

    def __init__(self, root: TreeNode):
        self.memo = set()
        self.recover(root, 0)

    def find(self, target: int) -> bool:
        return target in self.memo

    def recover(self, root, value):
        if not root:
            return
        root.val = value
        self.memo.add(value)

        if root.left:
            self.recover(root.left, 2 * value + 1)
        if root.right:
            self.recover(root.right, 2 * value + 2)

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)