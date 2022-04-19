class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        memo = {0:-1}
        pre_sum = 0
        for i, num in enumerate(nums):
            pre_sum += num
            pre_sum %= k
            if pre_sum in memo: 
                if i - memo[pre_sum] > 1:
                    return True
            else:
                memo[pre_sum] = i
        return False