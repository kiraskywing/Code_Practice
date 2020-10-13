class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] < nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        nums[i + 1:] = sorted(nums[i + 1:], reverse=True)
                        return nums
        nums.sort(reverse=True)
        return nums