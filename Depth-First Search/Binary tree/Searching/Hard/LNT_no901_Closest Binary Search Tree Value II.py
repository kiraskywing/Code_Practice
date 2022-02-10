"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """

    def closestKValues(self, root, target, k):

        if not root or k == 0:
            return []

        inorder = self.get_inorder(root)
        left = self.find_lower(inorder, target)
        right = left + 1
        result = []

        for _ in range(k):
            if self.left_is_closer(inorder, left, right, target):
                result.append(inorder[left])
                left -= 1
            else:
                result.append(inorder[right])
                right += 1

        return result

    def get_inorder(self, root):

        dummy = TreeNode(-1)
        dummy.right = root
        stack = [dummy]
        inorder = []

        while stack:
            node = stack.pop()

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

            if stack:
                inorder.append(stack[-1].val)

        return inorder

    def find_lower(self, inorder, target):
        left, right = 0, len(inorder) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if inorder[mid] < target:
                left = mid
            else:
                right = mid

        if inorder[left] < target:
            return left
        if inorder[right] < target:
            return right

        return -1

    def left_is_closer(self, inorder, left, right, target):
        if left < 0:
            return False
        if right >= len(inorder):
            return True

        return target - inorder[left] < inorder[right] - target
