class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums, 0, len(nums) - 2), self.helper(nums, 1, len(nums) - 1))
    
    def helper(self, nums, start, end):
        pre_include = pre_exclude = 0
        for i in range(start, end + 1):
            cur_include = pre_exclude + nums[i]
            cur_exclude = max(pre_include, pre_exclude)
            pre_include, pre_exclude = cur_include, cur_exclude
        
        return max(cur_include, cur_exclude)