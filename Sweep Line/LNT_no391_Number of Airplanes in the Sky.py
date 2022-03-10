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
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def count_of_airplanes(self, airplanes: List[Interval]) -> int:
        temp = []
        for itv in airplanes:
            temp.append((itv.start, 1))
            temp.append((itv.end, -1))
        
        cur, res = 0, 0
        temp.sort()
        for _, val in temp:
            cur += val
            res = max(res, cur)
        return res
