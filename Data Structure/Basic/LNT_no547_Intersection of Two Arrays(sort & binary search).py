class Solution:
    """
    @param nums1: an integer array
    @param nums2: an integer array
    @return: an integer array
    """

    def intersection(self, nums1, nums2):
        if not nums1 or not nums2:
            return []

        nums1.sort()
        length = len(nums1)
        visited, result = set(), []

        for i in nums2:
            if i not in visited and self.binary_search(nums1, length, i):
                visited.add(i)
                result.append(i)

        return result

    def binary_search(self, array, length, target):
        left, right = 0, length - 1

        while left + 1 < right:
            mid = (left + right) // 2
            if array[mid] < target:
                left = mid
            elif array[mid] > target:
                right = mid
            else:
                return True

        if array[left] == target:
            return True
        if array[right] == target:
            return True

        return False