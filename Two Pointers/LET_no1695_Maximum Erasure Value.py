class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        memo = collections.defaultdict(int)
        res = temp = j = 0
        
        for i in range(len(nums)):
            memo[nums[i]] += 1
            temp += nums[i]
            while memo[nums[i]] > 1:
                memo[nums[j]] -= 1
                temp -= nums[j]
                j += 1
            res = max(res, temp)
        
        return res
            