class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        memo = collections.defaultdict(int)
        memo[0] = 1
        cur, res = 0, 0
        for num in nums:
            cur += num
            res += memo[cur - goal]
            memo[cur] += 1
        
        return res