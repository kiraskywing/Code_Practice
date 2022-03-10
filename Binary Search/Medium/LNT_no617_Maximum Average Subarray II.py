# The same as LeetCode no644. Maximum Average Subarray II

class Solution:
    """
    @param nums: an array with positive and negative Numbers
    @param k: an integer
    @return: the maximum average
    """

    def maxAverage(self, nums, k):
        if not nums:
            return 0

        start, end = min(nums), max(nums)
        while end - start > 1e-5:
            mid = (start + end) / 2
            if self.check_subarray(nums, k, mid):
                start = mid
            else:
                end = mid
        return start

    def check_subarray(self, nums, k, average):
        cur, pre, pre_min = 0, 0, 0
        for i in range(k - 1):
            cur += nums[i] - average
            
        for i in range(k - 1, len(nums)):
            cur += nums[i] - average
            if cur - pre_min >= 0:
                return True
            pre += nums[i - k + 1] - average
            pre_min = min(pre_min, pre)
        
        return False
