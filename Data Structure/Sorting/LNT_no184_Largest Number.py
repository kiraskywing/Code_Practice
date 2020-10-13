from functools import cmp_to_key

class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """

    def largestNumber(self, nums):

        self.temp = [0 for _ in range(len(nums))]

        if nums == self.temp:
            return "0"

        lst = [str(x) for x in nums]
        res = self.mergesort(lst, 0, len(lst) - 1)

        return "".join(res)

    def mergesort(self, lst, left, right):

        if left >= right:
            return lst

        mid = (left + right) // 2
        self.mergesort(lst, left, mid)
        self.mergesort(lst, mid + 1, right)
        self.merge(lst, left, right)

        return lst

    def merge(self, lst, left, right):

        mid = (left + right) // 2
        i_L, i_R, index = left, mid + 1, left

        while i_L <= mid and i_R <= right:
            if str(lst[i_L]) + str(lst[i_R]) > str(lst[i_R]) + str(lst[i_L]):
                self.temp[index] = lst[i_L]
                i_L += 1
            else:
                self.temp[index] = lst[i_R]
                i_R += 1
            index += 1

        while i_L <= mid:
            self.temp[index] = lst[i_L]
            i_L += 1
            index += 1
        while i_R <= right:
            self.temp[index] = lst[i_R]
            i_R += 1
            index += 1

        for i in range(left, right + 1):
            lst[i] = self.temp[i]

        """
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x) + str(y) < str(y) + str(x) else -1))

        if nums[0] == 0:
            return '0'

        return "".join([str(x) for x in nums])
        """