class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        temp = []
        for left, right in intervals:
            temp.append((left, 1))
            temp.append((right, -1))
        
        cur, res = 0, 0
        temp.sort()
        for _, val in temp:
            cur += val
            res = max(res, cur)
        
        return res