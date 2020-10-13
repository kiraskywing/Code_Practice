class Solution:
    """
    @param nums: a continuous stream of numbers
    @param number: a number
    @return: returns the first unique number
    """

    def firstUniqueNumber(self, nums, number):
        counter = collections.defaultdict(int)
        for num in nums:
            counter[num] += 1
            if num == number:
                break

        if number not in counter:
            return -1

        for num in nums:
            if counter[num] == 1:
                return num
            if num == number:
                break
        return -1
