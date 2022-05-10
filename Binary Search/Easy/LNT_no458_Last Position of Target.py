class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """

    def lastPosition(self, nums, target):

        if not nums:
            return -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:

            mid = (start + end) // 2

            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        if nums[start] == target:
            return start

        return -1


import bisect
class Solution2:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def last_position(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        i = bisect.bisect_right(nums, target)
        return i - 1 if nums[i - 1] == target else -1