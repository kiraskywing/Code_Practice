"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {ListNode[]} a lists of linked list
    def binaryTreeToLists(self, root):

        if not root:
            return []

        from queue import Queue

        temp = Queue()
        temp.put(root)
        res = []

        while not temp.empty():

            n = temp.qsize()
            dummy = ListNode(-1)
            cur = dummy

            for i in range(n):

                node = temp.get()
                cur.next = ListNode(node.val)
                cur = cur.next

                if node.left:
                    temp.put(node.left)
                if node.right:
                    temp.put(node.right)

            res.append(dummy.next)

        return res