class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        
        return dp[-1]

class Solution2:
    def rob(self, nums: List[int]) -> int:
        pre, pre_not, cur = 0, 0, 0
        for num in nums:
            cur = max(pre, pre_not + num)
            pre_not, pre, cur = pre, cur, 0
        return pre