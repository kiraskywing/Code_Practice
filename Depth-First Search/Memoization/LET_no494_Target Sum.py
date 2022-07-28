class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.dfs(nums, 0, target, {})
    
    def dfs(self, nums, i, target, memo):
        if i == len(nums):
            return int(target == 0)
        
        if (i, target) not in memo:
            a = self.dfs(nums, i + 1, target - nums[i], memo)
            b = self.dfs(nums, i + 1, target + nums[i], memo)
            memo[(i, target)] = a + b
        
        return memo[(i, target)]