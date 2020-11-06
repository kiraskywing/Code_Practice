"""
Definition of ArrayReader
class ArrayReader(object):
    def get(self, index):
    	# return the number on given index,
        # return 2147483647 if the index is invalid.
"""


class Solution:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """

    def searchBigSortedArray(self, reader, target):

        index = 0
        while reader.get(index) < target:
            index = index * 2 + 1

        left, right = 0, index

        while left + 1 < right:
            mid = (left + right) // 2

            if reader.get(mid) >= target:
                right = mid
            else:
                left = mid

        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right

        return -1