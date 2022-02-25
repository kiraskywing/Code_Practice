"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        if not intervals:
            return []

        return self.helper(intervals, 0, len(intervals) - 1)
    
    def helper(self, intervals, start, end):
        if start >= end:
            return intervals[start]

        mid = (start + end) // 2
        first = self.helper(intervals, start, mid)
        second = self.helper(intervals, mid + 1, end)
        return self.merge(first, second)

    def merge(self, a, b):
        res = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i].start < b[j].start:
                self.update(res, a[i])
                i += 1
            else:
                self.update(res, b[j])
                j += 1
        while i < len(a):
            self.update(res, a[i])
            i += 1
        while j < len(b):
            self.update(res, b[j])
            j += 1
        return res

    def update(self, cur, node):
        if not cur or cur[-1].end < node.start:
            cur.append(node)
        else:
            cur[-1].end = max(cur[-1].end, node.end)