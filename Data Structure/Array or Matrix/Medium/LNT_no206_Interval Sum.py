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
    @param a: An integer list
    @param queries: An query list
    @return: The result list
    """
    def interval_sum(self, a: List[int], queries: List[Interval]) -> List[int]:
        memo = [0] * (len(a) + 1)
        for i, num in enumerate(a):
            memo[i + 1] = num + memo[i]
        
        res = []
        for q in queries:
            res.append(memo[q.end + 1] - memo[q.start])
        return res
