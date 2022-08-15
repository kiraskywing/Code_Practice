from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Node:
    def __init__(self, i, j):
        self.i, self.j = i, j
        self.left = self.right = None
        self.val = 0

class SegmentTree:
    def __init__(self, nums):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, i, j):
        if i == j:
            cur = Node(i, i)
            cur.val = nums[i]
            return cur

        cur = Node(i, j)
        mid = (i + j) // 2
        cur.left = self.build(nums, i, mid)
        cur.right = self.build(nums, mid + 1, j)
        cur.val = cur.left.val + cur.right.val
        return cur

    def query(self, node, i, j):
        if node.i == i and node.j == j:
            return node.val
        
        mid = (node.i + node.j) // 2
        if j <= mid:
            return self.query(node.left, i, j)
        elif i >= mid + 1:
            return self.query(node.right, i, j)
        return self.query(node.left, i, mid) + self.query(node.right, mid + 1, j)

class Solution:
    """
    @param a: An integer list
    @param queries: An query list
    @return: The result list
    """
    def interval_sum(self, a: List[int], queries: List[Interval]) -> List[int]:
        sg = SegmentTree(a)
        res = []
        for itv in queries:
            res.append(sg.query(sg.root, itv.start, itv.end))
        return res
