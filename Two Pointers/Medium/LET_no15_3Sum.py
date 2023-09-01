class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j, k = i + 1, n - 1
            while j < k:
                cur = nums[j] + nums[k]
                if cur == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j > i + 1 and j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while k < n - 1 and j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif cur < target:
                    j += 1
                    while j > i + 1 and j < k  and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while k < n - 1 and j < k and nums[k] == nums[k + 1]:
                        k -= 1
        
        return res