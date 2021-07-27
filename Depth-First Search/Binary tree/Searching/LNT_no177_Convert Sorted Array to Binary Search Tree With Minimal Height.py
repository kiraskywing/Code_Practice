# The same as LeetCode no108. Convert Sorted Array to Binary Search Tree

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param: A: an integer array
    @return: A tree node
    """
    def sortedArrayToBST(self, A):

        if not A:
            return None

        return self.convert(A, 0, len(A) - 1)

    def convert(self, A, start, end):

        if start > end:
            return
        if start == end:
            return TreeNode(A[start])

        mid = (start + end) // 2
        root = TreeNode(A[mid])

        root.left = self.convert(A, start, mid - 1)
        root.right = self.convert(A, mid + 1, end)

        return root