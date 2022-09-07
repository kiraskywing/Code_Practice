class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # empty nums? => no
        # range of k? => negative, 0, and positive integer
        
        # Approach:
        # use a hashmap with (key, value) pair as (prefix_sum, minimum_index)
        # (prefix_sum, prefix_sum - k) => (right, left) => length = right - left
        # e.g. nums = [1,-1,5,-2,3], k = 3 => prefix_sum = [0, 1, 0, 5, 3, 6]
        #   => memo = {0:-1, 1:0, 5:2, 3:3, 6:4} => max_length = 3 - (-1) = 4
        
        memo = {0:-1}    # Space: O(n)
        prefix_sum = 0
        res = 0
        for i, num in enumerate(nums):    # Time: O(n)
            prefix_sum += num
            if prefix_sum - k in memo:    # Time: O(1)
                res = max(res, i - memo[prefix_sum - k])
            if prefix_sum not in memo:    # Time: O(1)
                memo[prefix_sum] = i
        
        return res