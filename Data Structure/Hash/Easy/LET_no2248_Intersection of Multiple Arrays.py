class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        m = len(nums)
        memo = collections.defaultdict(int)
        res = []
        for row in nums:
            for num in row:
                memo[num] += 1
                if memo[num] == m:
                    res.append(num)
        return sorted(res)