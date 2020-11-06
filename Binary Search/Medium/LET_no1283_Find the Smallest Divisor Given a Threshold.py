class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            if sum(int(math.ceil(num / mid)) for num in nums) > threshold:
                left = mid
            else:
                right = mid

        if sum(int(math.ceil(num / left)) for num in nums) <= threshold:
            return left
        return right