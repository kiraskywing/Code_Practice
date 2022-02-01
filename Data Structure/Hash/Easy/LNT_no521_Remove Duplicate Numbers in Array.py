class Solution:
    """
    @param nums: an array of integers
    @return: the number of unique integers
    """

    def deduplication(self, nums):
        temp, res = set(), 0
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp.add(nums[i])
                nums[res] = nums[i]
                res += 1

        return res
