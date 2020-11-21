# The same as Leetcode no81. Search in Rotated Sorted Array II

class Solution:
    """
    @param A: an integer ratated sorted array and duplicates are allowed
    @param target: An integer
    @return: a boolean
    """

    def search(self, A, target):
        if not A:
            return False

        for num in A:
            if num == target:
                return True

        return False
