class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        location = 0
        res = 0
        for i in range(1, len(nums) - 1):
            if nums[i] > nums[location] and nums[i] > nums[i + 1] or \
               nums[i] < nums[location] and nums[i] < nums[i + 1]:
                res += 1
                location = i
        
        return res