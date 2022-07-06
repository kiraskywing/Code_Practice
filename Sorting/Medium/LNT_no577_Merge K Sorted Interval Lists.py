"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        heap = []
        for i, node in enumerate(intervals):
            if not node:
                continue
            heapq.heappush(heap, (node[0].start, node[0].end, i, 0))
        
        res = []
        while heap:
            start, end, i, j = heapq.heappop(heap)
            self.helper(res, start, end)
            j += 1
            if j < len(intervals[i]):
                heapq.heappush(heap, (intervals[i][j].start, intervals[i][j].end, i, j))
        
        return res

    def helper(self, res, start, end):
        if not res or res[-1].end < start:
            res.append(Interval(start, end))
            return
        
        res[-1].end = max(res[-1].end, end)
