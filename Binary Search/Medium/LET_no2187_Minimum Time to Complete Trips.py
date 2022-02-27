class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        total_t_min, total_t_max = 1, min(time) * totalTrips
        while total_t_min + 1 < total_t_max:
            mid = (total_t_min + total_t_max) // 2
            if self.countTrips(time, mid) < totalTrips:
                total_t_min = mid
            else:
                total_t_max = mid
        
        if self.countTrips(time, total_t_min) >= totalTrips:
            return total_t_min
        return total_t_max
    
    def countTrips(self, time, target):
        return sum(target // t for t in time)