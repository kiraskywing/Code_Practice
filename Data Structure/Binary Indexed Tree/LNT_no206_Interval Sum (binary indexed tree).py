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

class Bit:
    def __init__(self, nums):
        self.size = len(nums) + 1
        self.nums = [0] * self.size
        self.bit = [0] * self.size
        for i, num in enumerate(nums):
            self.update(i, num)

    def update(self, idx, num):
        idx += 1
        diff = num - self.nums[idx]
        self.nums[idx] = num

        while idx < self.size:
            self.bit[idx] += diff
            idx += (idx & -idx)

    def query(self, idx):
        res = 0
        idx += 1
        while idx > 0:
            res += self.bit[idx]
            idx -= (idx & -idx)
        return res

class Solution:
    """
    @param a: An integer list
    @param queries: An query list
    @return: The result list
    """
    def interval_sum(self, a: List[int], queries: List[Interval]) -> List[int]:
        bt = Bit(a)
        res = []
        for itv in queries:
            res.append(bt.query(itv.end) - bt.query(itv.start - 1))
        return res
