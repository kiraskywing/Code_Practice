class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        memo = collections.Counter(nums)
        res = 0
        for num in memo:
            if k == 0 and memo[num] > 1:
                res += 1
            if k > 0 and num + k in memo:
                res += 1
        return res