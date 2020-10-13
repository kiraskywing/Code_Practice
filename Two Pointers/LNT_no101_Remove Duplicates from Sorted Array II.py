class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """

    def removeDuplicates(self, nums):
        if not nums:
            return 0

        left, count = 0, 1
        for right in range(1, len(nums)):
            if nums[left] == nums[right]:
                count += 1
            else:
                count = 1

            if count <= 2:
                left += 1
                nums[left] = nums[right]

        return left + 1