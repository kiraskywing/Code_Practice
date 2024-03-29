class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        diff = nums[-1] - nums[0] + 1
        missing = diff - len(nums)
        if k > missing:
            return nums[-1] + k - missing
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            missing = nums[mid] - nums[left] - (mid - left)
            if missing < k:
                left = mid
                k -= missing
            else:
                right = mid
        
        return nums[left] + k

class Solution2:
    def missingElement(self, nums: List[int], k: int) -> int:
        for i in range(1, len(nums)):
            diff = min(nums[i] - nums[i - 1] - 1, k)
            k -= diff
            if k == 0:
                return nums[i - 1] + diff
        
        return nums[-1] + k