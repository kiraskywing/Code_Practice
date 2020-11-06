class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if mid <= nums[mid]:
                left = mid
            else:
                right = mid
        if right + 1 <= nums[right]:
            return right + 1
        if left + 1 <= nums[left]:
            return left + 1
        return -1