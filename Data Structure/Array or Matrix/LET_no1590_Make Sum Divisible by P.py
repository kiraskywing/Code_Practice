class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        need = sum(nums) % p
        rec = {0 : -1}
        cur = 0
        res = n = len(nums)
        
        for i, num in enumerate(nums):
            cur = (cur + num) % p
            rec[cur] = i
            if (cur - need) % p in rec:
                res = min(res, i - rec[(cur - need) % p])
        
        return res if res < n else -1