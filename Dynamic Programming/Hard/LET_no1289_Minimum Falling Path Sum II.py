# Given a square grid of integers arr, a falling path with non-zero shifts
# is a choice of exactly one element from each row of arr, such that no two
# elements chosen in adjacent rows are in the same column.
# Return the minimum sum of a falling path with non-zero shifts.

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        for i in range(1, len(arr)):
            r = sorted(arr[i - 1])
            for j in range(len(arr[0])):
                arr[i][j] += r[1] if r[0] == arr[i - 1][j] else r[0]

        return min(arr[-1])