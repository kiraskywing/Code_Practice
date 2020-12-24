class Solution:
    """
    @param nums: An array of integers
    @return: nothing
    """

    def nextPermutation(self, nums):
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]

                        left, right = i + 1, len(nums) - 1
                        while left <= right:
                            nums[left], nums[right] = nums[right], nums[left]
                            left += 1
                            right -= 1

                        return nums

        nums.reverse()
        return nums