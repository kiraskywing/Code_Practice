class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        return self.dfs(total // 2, nums, 0, {})
    
    def dfs(self, target, nums, i, memo):
        if target < 0 :
            return False
        
        if i == len(nums):
            return target == 0
        
        if (target, i) not in memo:
            memo[(target, i)] = self.dfs(target - nums[i], nums, i + 1, memo) or self.dfs(target, nums, i + 1, memo)
        
        return memo[(target, i)]