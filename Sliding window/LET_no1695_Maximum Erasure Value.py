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

class Solution2:
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