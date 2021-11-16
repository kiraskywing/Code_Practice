class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def enough(num):
            return sum(min(num // i, n) for i in range(1, m + 1)) >= k
        
        low, high = 1, m * n
        while low + 1 < high:
            mid = (low + high) // 2
            if not enough(mid):
                low = mid
            else:
                high = mid
        
        if enough(low):
            return low
        return high