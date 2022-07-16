class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """

    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        i = reach = 0
        while i < n and i <= reach:
            reach = max(reach, i + nums[i])
            i += 1
        return i == n
