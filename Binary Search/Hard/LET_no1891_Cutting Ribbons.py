class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        left, right = 1, max(ribbons)
        while left + 1 < right:
            mid = (left + right) // 2
            if self.helper(ribbons, mid) >= k:
                left = mid
            else:
                right = mid
        
        if self.helper(ribbons, right) >= k:
            return right
        if self.helper(ribbons, left) >= k:
            return left
        return 0
    
    def helper(self, arr, target):
        return sum(num // target for num in arr)