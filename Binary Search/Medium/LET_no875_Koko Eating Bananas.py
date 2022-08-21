class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val, max_val = 1, max(piles)
        while min_val + 1 < max_val:
            mid_val = (min_val + max_val) // 2
            if self.getTotalHours(piles, mid_val) > h:
                min_val = mid_val
            else:
                max_val = mid_val
                
        if self.getTotalHours(piles, min_val) <= h:
            return min_val
        return max_val
    
    def getTotalHours(self, piles, val):
        return sum(math.ceil(p / val) for p in piles)