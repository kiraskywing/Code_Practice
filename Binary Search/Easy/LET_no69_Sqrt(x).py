class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left + 1 < right:
            mid = (left + right) // 2
            if x <= mid ** 2:
                right = mid
            else:
                left = mid
        
        return right if right ** 2 <= x else left