class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left + 1 < right:
            mid = (left + right) // 2
            cur = sum(ceil(p / mid) for p in piles)
            if cur > h:
                left = mid
            else:
                right = mid
        
        cur = sum(ceil(p / left) for p in piles)
        if cur < h:
            return left
        return right