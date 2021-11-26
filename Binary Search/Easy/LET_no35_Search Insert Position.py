class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums) - 1
        while i + 1 < j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid
            else:
                j = mid
        
        if nums[i] >= target:
            return i
        elif nums[j] >= target:
            return j
        return j + 1