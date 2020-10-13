class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):

        item_sum = [(0, -1)]

        for i, val in enumerate(nums):
            item_sum.append((item_sum[-1][0] + val, i))

        item_sum.sort()
        min_diff = sys.maxsize
        ans = []

        for j in range(1, len(item_sum)):

            if abs(item_sum[j][0] - item_sum[j - 1][0]) < min_diff:
                min_diff = abs(item_sum[j][0] - item_sum[j - 1][0])

                index_L = min(item_sum[j][1], item_sum[j - 1][1]) + 1
                index_R = max(item_sum[j][1], item_sum[j - 1][1])

                ans = [index_L, index_R]

        return ans