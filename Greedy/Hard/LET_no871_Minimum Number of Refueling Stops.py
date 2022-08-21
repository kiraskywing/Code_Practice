class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        i = times = 0
        cur_pos = startFuel
        fuel_candidates = []
        
        while cur_pos < target:
            while i < len(stations) and stations[i][0] <= cur_pos:
                heapq.heappush(fuel_candidates, -stations[i][1])
                i += 1
                
            if not fuel_candidates:
                return -1
            
            cur_pos += -heapq.heappop(fuel_candidates)
            times += 1
        
        return times
                