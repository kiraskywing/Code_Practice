class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        m = len(triangle)
        
        for i in range(1, m):
            for j in range(len(triangle[i])):
                last = float('inf')
                if j < len(triangle[i - 1]):
                    last = min(last, triangle[i - 1][j])
                if j > 0:
                    last = min(last, triangle[i - 1][j - 1])
                triangle[i][j] += last
        
        return min(triangle[m - 1])
