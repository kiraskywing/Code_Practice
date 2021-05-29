class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = cur = 0
        seen = set()
        i = 0
        for j in range(len(nums)):
            while i < j and nums[j] in seen:
                seen.remove(nums[i])
                cur -= nums[i]
                i += 1
            seen.add(nums[j])
            cur += nums[j]
            res = max(res, cur)
        
        return res