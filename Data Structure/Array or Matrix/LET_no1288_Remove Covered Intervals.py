class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda a: (a[0], -a[1]))
        result = 1
        upper = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][1] > upper:
                upper = intervals[i][1]
                result += 1

        return result