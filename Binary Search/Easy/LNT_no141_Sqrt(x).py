# The same as LeetCode no69. Sqrt(x)

class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if mid * mid > x:
                end = mid
            else:
                start = mid

        if end * end <= x:
            return end
        return start
