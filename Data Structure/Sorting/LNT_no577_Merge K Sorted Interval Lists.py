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
        for index, array in enumerate(intervals):
            if not array:
                continue
            heapq.heappush(heap, (array[0].start, array[0].end, index, 0))

        result = []
        while heap:
            start, end, index, i_array = heapq.heappop(heap)
            self.append_and_merge(result, Interval(start, end))
            if i_array + 1 < len(intervals[index]):
                heapq.heappush(heap, (
                intervals[index][i_array + 1].start, intervals[index][i_array + 1].end, index, i_array + 1))

        return result

    def append_and_merge(self, result, interval):
        if not result:
            result.append(interval)
            return

        last_interval = result[-1]
        if last_interval.end < interval.start:
            result.append(interval)
            return

        last_interval.end = max(last_interval.end, interval.end)