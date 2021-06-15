class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        if not arrays:
            return []

        while len(arrays) > 1:
            next_arrays = []

            for i in range(0, len(arrays), 2):
                if i + 1 < len(arrays):
                    new_array = self.merge_two_arrays(arrays[i], arrays[i + 1])
                else:
                    new_array = arrays[i]
                next_arrays.append(new_array)

            arrays = next_arrays

        return arrays[0]

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