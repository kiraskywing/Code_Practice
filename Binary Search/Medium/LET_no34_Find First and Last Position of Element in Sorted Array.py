class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        return [self.findFirst(nums, target, True), self.findFirst(nums, target, False)]
    
    def findFirst(self, nums, target, first):
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if first:
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] <= target:
                    left = mid
                else:
                    right = mid
        
        if first:
            if nums[left] == target: return left
            if nums[right] == target: return right
        else:
            if nums[right] == target: return right
            if nums[left] == target: return left
        return -1