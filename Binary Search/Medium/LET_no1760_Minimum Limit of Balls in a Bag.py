class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum((num - 1) // mid for num in nums) > maxOperations:
                left = mid
            else:
                right = mid
        
        if sum((num - 1) // left for num in nums) <= maxOperations:
            return left
        return right