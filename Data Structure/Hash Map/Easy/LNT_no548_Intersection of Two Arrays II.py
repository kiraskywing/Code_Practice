# The same as LeetCode no350_Intersection of Two Arrays II

class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        memo = collections.defaultdict(int)
        result = []

        for i in nums1:
            memo[i] += 1

        for j in nums2:
            memo[j] -= 1
            if memo[j] >= 0:
                result.append(j)

        return result
