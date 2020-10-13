class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if not arrays:
            return []

        return self.merge_range_arrays(arrays, 0, len(arrays) - 1)

    def merge_range_arrays(self, arrays, left, right):
        if left >= right:
            return arrays[left]

        mid = (left + right) // 2
        sorted_L = self.merge_range_arrays(arrays, left, mid)
        sorted_R = self.merge_range_arrays(arrays, mid + 1, right)
        return self.merge_two_arrays(sorted_L, sorted_R)

    def merge_two_arrays(self, arr_a, arr_b):
        i, j, result = 0, 0, []

        while i < len(arr_a) and j < len(arr_b):
            if arr_a[i] < arr_b[j]:
                result.append(arr_a[i])
                i += 1
            else:
                result.append(arr_b[j])
                j += 1

        while i < len(arr_a):
            result.append(arr_a[i])
            i += 1
        while j < len(arr_b):
            result.append(arr_b[j])
            j += 1

        return result
