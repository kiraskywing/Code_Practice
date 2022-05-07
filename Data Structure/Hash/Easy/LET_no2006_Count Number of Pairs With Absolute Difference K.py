class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        memo = collections.defaultdict(int)
        res = 0
        for num in nums:
            a, b = num - k, num + k
            res += memo[a] + memo[b]
            memo[num] += 1
                
        return res