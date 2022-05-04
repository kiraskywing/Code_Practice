class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        left, right = 0, n - 1
        while left + 1 < n and nums[left] <= nums[left + 1]:
            left += 1
        while right > 0 and nums[right] >= nums[right - 1]:
            right -= 1
        
        if right <= left:
            return 0
        
        min_val, max_val = self.helper(nums, left, right)
        while left > 0 and nums[left - 1] > min_val:
            left -= 1
        while right + 1 < n and nums[right + 1] < max_val:
            right += 1
        
        return right - left + 1
        
    
    def helper(self, nums, left, right):
        min_val, max_val = float('inf'), float('-inf')
        for i in range(left, right + 1):
            min_val = min(min_val, nums[i])
            max_val = max(max_val, nums[i])
        return min_val, max_val