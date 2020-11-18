class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        
        res = []
        
        for interval in sorted(intervals, key=lambda x : x[0]):
            if res and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
        
        return res