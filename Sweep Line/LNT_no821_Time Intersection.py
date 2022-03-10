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

class Solution:
    """
    @param seq_a: the list of intervals
    @param seq_b: the list of intervals
    @return: the time periods
    """
    def time_intersection(self, seq_a: List[Interval], seq_b: List[Interval]) -> List[Interval]:
        seq = []
        for itv in seq_a + seq_b:
            seq.append((itv.start, 1))
            seq.append((itv.end, -1))
        seq.sort()

        cur = 0
        res, temp = [], []
        for time, val in seq:
            pre = cur
            cur += val
            if cur == 2:
                temp.append(time)
            elif cur == 1 and pre == 2:
                temp.append(time)
                res.append(Interval(temp[0], temp[1]))
                temp = []
        return res
