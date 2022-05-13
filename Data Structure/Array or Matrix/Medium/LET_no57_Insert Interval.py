class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        res = []
        i = j = 0
        while i < n or j == 0:
            if j > 0 or i < n and intervals[i][0] < newInterval[0]:
                self.helper(res, intervals[i][0], intervals[i][1])
                i += 1
            else:
                self.helper(res, newInterval[0], newInterval[1])
                j += 1
        return res
    
    def helper(self, res, start, end):
        if not res or start > res[-1][1]:
            res.append([start, end])
        else:
            res[-1][1] = max(res[-1][1], end)

class Solution2:
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