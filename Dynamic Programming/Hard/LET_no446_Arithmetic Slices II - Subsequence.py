class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        res = 0
        dp = [collections.defaultdict(int) for _ in range(len(nums))]
        
        for i in range(len(nums)):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += dp[j][diff] + 1
                res += dp[j][diff]
        
        return res