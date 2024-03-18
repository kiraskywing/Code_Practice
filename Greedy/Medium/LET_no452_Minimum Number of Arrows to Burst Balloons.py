class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key = lambda x: x[1])
        res, end = 0, -sys.maxsize
        
        for left, right in points:
            if left > end:
                res += 1
                end = right
        
        return res