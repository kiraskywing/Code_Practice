class Solution:
    """
    @param nums: an array of Integer
    @param target: target = nums[index1] + nums[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, nums, target):

        left, right = 0, len(nums) - 1

        while left < right:
            value = nums[left] + nums[right]

            if value > target:
                right -= 1
            elif value < target:
                left += 1
            else:
                return [left + 1, right + 1]

        return []