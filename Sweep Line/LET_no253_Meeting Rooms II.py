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

class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        cur = res = 0
        heap = []
        for start, end in intervals:
            heapq.heappush(heap, (start, 1))
            heapq.heappush(heap, (end, -1))
            
        while heap:
            time, val = heapq.heappop(heap)
            cur += val
            res = max(res, cur)
        
        return res