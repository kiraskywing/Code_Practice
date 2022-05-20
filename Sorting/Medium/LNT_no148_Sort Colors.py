# the same as LeetCode no75. Sort Colors

class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2
    @return: nothing
    """
    def sortColors(self, nums):
        index = self.sorter(nums, 0, 0)
        self.sorter(nums, index, 1)

    def sorter(self, nums, start, flag):
        left, right = start, len(nums) - 1

        while left <= right:
            while left <= right and nums[left] == flag:
                left += 1
            while left <= right and nums[right] != flag:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        return left

class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = p1 = 0
        p2 = len(nums) - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1