class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        n = len(timeSeries)
        if n == 0:
            return 0
        if n == 1:
            return duration
        
        res = 0
        start, end = timeSeries[0], timeSeries[0] + duration
        for i in range(1, n):
            if timeSeries[i] > end:
                res += end - start
                start = timeSeries[i]
            end = timeSeries[i] + duration
        res += (end - start)
        return res