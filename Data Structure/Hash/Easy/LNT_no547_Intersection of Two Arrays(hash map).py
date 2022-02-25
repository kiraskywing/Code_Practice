class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        hash_1, hash_2, result = set(nums1), set(nums2), []
        result = [i for i in hash_1 if i in hash_2]
        return result