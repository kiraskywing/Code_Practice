import heapq

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = [(L, -H, R) for L, R, H in buildings]
        events += list({(R, 0, 0) for _, R, _ in buildings})
        events.sort()
        
        res = [[0, 0]]    # [x, height]
        temp = [(0, sys.maxsize)]    # [height, R]
        
        for left, negH, right in events:
            while left >= temp[0][1]:   #. x position swaps to new building
                heapq.heappop(temp)
            if negH:
                heapq.heappush(temp, (negH, right))
            if -temp[0][0] != res[-1][1]:   # height jump detected
                res.append([left, -temp[0][0]])
        
        return res[1:]