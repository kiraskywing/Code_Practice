"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """

    def mergeTwoInterval(self, list1, list2):
        i, j, result = 0, 0, []

        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(result, list1[i])
                i += 1
            else:
                self.push_back(result, list2[j])
                j += 1

        while i < len(list1):
            self.push_back(result, list1[i])
            i += 1
        while j < len(list2):
            self.push_back(result, list2[j])
            j += 1

        return result

    def push_back(self, result, interval):
        if not result:
            result.append(interval)
            return

        last_interval = result[-1]
        if interval.start > last_interval.end:
            result.append(interval)
            return
        last_interval.end = max(last_interval.end, interval.end)