class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """

    def twoSum6(self, nums, target):
        n = len(nums)
        if n < 2:
            return 0

        nums.sort()
        left, right = 0, n - 1
        count = 0
        while left < right:
            value = nums[left] + nums[right]
            if value == target:
                count += 1
                left += 1
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

            elif value > target:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            else:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

        return count
