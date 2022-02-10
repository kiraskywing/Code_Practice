class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        memo = collections.defaultdict(int)
        preSum = 0
        memo[preSum] += 1
        res = 0
        for num in nums:
            preSum += num
            res += memo[preSum - k]
            memo[preSum] += 1
        return res