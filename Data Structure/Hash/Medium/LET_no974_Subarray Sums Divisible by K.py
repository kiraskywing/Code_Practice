class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        memo = [0 for _ in range(k)]
        memo[0] = 1
        res = prefix_sum = 0

        for num in nums:
            prefix_sum = ((prefix_sum + num) % k + k) % k
            res += memo[prefix_sum]
            memo[prefix_sum] += 1

        return res