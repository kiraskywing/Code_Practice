class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.count(weights, mid) > days:
                left = mid
            else:
                right = mid
                
        if self.count(weights, left) <= days:
            return left
        return right
    
    def count(self, weights, limit):
        res = cur = 0
        for w in weights:
            if cur + w > limit:
                res += 1
                cur = 0
            cur += w
        return res + 1