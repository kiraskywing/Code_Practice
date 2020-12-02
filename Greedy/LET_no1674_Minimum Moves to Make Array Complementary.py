class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        delta = collections.defaultdict(int)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            delta[2] += 2
            delta[min(a, b) + 1] -= 1
            delta[a + b] -= 1
            delta[a + b + 1] += 1
            delta[max(a, b) + limit + 1] += 1
        
        res, cur = sys.maxsize, 0
        for i in range(2, limit * 2 + 1):
            cur += delta[i]
            res = min(res, cur)
        
        return res