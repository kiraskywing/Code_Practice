class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        cur = 0
        res = []
        
        while cur < n and intervals[cur][1] < newInterval[0]:
            res.append(intervals[cur])
            cur += 1
        
        while cur < n and intervals[cur][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[cur][0])
            newInterval[1] = max(newInterval[1], intervals[cur][1])
            cur += 1
        
        res.append(newInterval)
        res.extend(intervals[cur:])
        
        return res