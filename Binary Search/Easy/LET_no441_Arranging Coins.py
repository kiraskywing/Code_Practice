class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        while low + 1 < high:
            mid = (low + high) // 2
            cur = mid * (mid + 1) // 2
            if cur <= n:
                low = mid
            else:
                high = mid
        
        cur = high * (high + 1) // 2
        if cur <= n:
            return high
        return low