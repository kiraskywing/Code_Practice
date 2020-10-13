"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    """
    @param root: the root of the binary tree
    @param level: the depth of the target level
    @return: An integer
    """
    def levelSum(self, root, level):

        self.res = 0
        self.count(root, level, 1)
        return self.res

    def count(self, root, level, height):
        if not root:
            return

        if height == level:
            self.res += root.val
            return

        self.count(root.left, level, height + 1)
        self.count(root.right, level, height + 1)

        """    
        if not root:
            return 0

        res = 0
        height = 1
        from queue import Queue
        tmp = Queue()
        tmp.put(root)

        while not tmp.empty():
            if height == level:
                break

            n = tmp.qsize()
            for i in range(n):
                cur = tmp.get()
                if cur.left:
                    tmp.put(cur.left)
                if cur.right:
                    tmp.put(cur.right)

            height += 1

        while not tmp.empty():
            cur = tmp.get()
            res += cur.val

        return res
        """