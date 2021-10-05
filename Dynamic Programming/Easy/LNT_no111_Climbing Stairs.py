# The same as LeetCode no70. Climbing Stairs

class Solution:
    """
    @param n: An integer
    @return: An integer
    """

    def climbStairs(self, n):
        if n <= 2:
            return n

        result = [1, 2] + [0] * (n - 2)

        for i in range(2, n):
            result[i] = result[i - 1] + result[i - 2]
        return result[-1]
