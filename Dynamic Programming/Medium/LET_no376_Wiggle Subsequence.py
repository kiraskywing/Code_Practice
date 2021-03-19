class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        dp_up = [1] * len(nums)
        dp_down = [1] * len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 0:
                dp_up[i] = dp_down[i - 1] + 1
                dp_down[i] = dp_down[i - 1]
            elif nums[i] - nums[i - 1] < 0:
                dp_down[i] = dp_up[i - 1] + 1
                dp_up[i] = dp_up[i - 1]
            else:
                dp_up[i] = dp_up[i - 1]
                dp_down[i] = dp_down[i - 1]
        
        return res