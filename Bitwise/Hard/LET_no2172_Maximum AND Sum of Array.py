class Solution:
    def maximumANDSum(self, nums: List[int], numSlots: int) -> int:
        mask = 3 ** numSlots - 1
        memo = [0 for _ in range(mask + 1)]
        return self.dfs(nums, memo, len(nums) - 1, mask, numSlots)
    
    def dfs(self, nums, memo, idx, mask, numSlots):
        if memo[mask] > 0:
            return memo[mask]
        if idx < 0:
            return 0
        
        bit, slot = 1, 1
        while slot <= numSlots:
            if mask // bit % 3 > 0:
                memo[mask] = max(memo[mask], (nums[idx] & slot) + self.dfs(nums, memo, idx - 1, mask - bit, numSlots))
            bit *= 3
            slot += 1
        return memo[mask]
            