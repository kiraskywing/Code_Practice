class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        for i in range(len(buildings)):
            buildings.append([buildings[i][1], 0, 0])    # append([R, 0, 0])
        
        buildings.sort(key=lambda x: (x[0], -x[2]))    # sorted by (left, -height)
        res = []
        temp = []
        for left, right, height in buildings:
            while temp and temp[0][1] <= left:    # x position sweeps to new building
                heapq.heappop(temp)
            heapq.heappush(temp, (-height, right))
            if not res or res[-1][1] != -temp[0][0]:    # height jump detected
                res.append([left, -temp[0][0]])
        
        return res