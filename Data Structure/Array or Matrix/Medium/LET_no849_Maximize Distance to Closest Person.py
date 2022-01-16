class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last = 0, -1
        
        for i in range(len(seats)):
            if seats[i]:
                res = max(res, i if last < 0 else (i - last) // 2)
                last = i
        
        return max(res, len(seats) - 1 - last)