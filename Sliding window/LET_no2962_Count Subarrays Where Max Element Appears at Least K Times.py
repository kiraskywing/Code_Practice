class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        left = cur = res = 0
        for right in range(len(nums)):
            cur += nums[right] == max_val
            while cur >= k:
                cur -= nums[left] == max_val
                left += 1
            res += left
        
        return res
