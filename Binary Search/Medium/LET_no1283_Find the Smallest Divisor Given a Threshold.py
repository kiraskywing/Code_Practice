class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        min_val, max_val = 1, max(nums)
        while min_val + 1 < max_val:
            mid_val = (min_val + max_val) // 2
            if self.getSum(nums, mid_val) <= threshold:
                max_val = mid_val
            else:
                min_val = mid_val
                
        if self.getSum(nums, min_val) <= threshold:
            return min_val
        return max_val
    
    def getSum(self, nums, divisor):
        return sum(math.ceil(num / divisor) for num in nums)