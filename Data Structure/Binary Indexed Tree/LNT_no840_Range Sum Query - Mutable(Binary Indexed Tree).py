# The same as LeetCode no307. Range Sum Query - Mutable

class NumArray:

    def __init__(self, nums):
        """
        :type nums: Array or Matrix[int]
        """
        self.array = nums
        self.length = len(nums)
        self.bit = [0] * (self.length + 1)
        for i in range(self.length):
            self.add(i, self.array[i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.add(i, val - self.array[i])
        self.array[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j) - self.sum(i - 1)

    def add(self, index, value):
        index += 1
        while index <= self.length:
            self.bit[index] += value
            index += (index & -index)

    def sum(self, index):
        index += 1
        result = 0

        while index > 0:
            result += self.bit[index]
            index -= (index & -index)

        return result

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)