class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = collections.defaultdict(int)
        memo[0] = 1
        
        for num in nums:
            memo2 = collections.defaultdict(int)
            for val, count in memo.items():
                memo2[val + num] += count
                memo2[val - num] += count
            memo = memo2
        
        return memo[target]