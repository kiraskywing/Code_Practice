class Solution:
    """
    @param matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
            
        m, n = len(matrix), len(matrix[0])
        max_rectangle = 0
        heights = [0] * (n + 1)
        heights[-1] = -1
        for row in matrix:
            indices_stack = []
            for right in range(n + 1):
                if right < n:
                    heights[right] = heights[right] + 1 if row[right] else 0
                
                while indices_stack and heights[indices_stack[-1]] > heights[right]:
                    idx = indices_stack.pop()
                    left = indices_stack[-1] if indices_stack else -1
                    max_rectangle = max(max_rectangle, (right - left - 1) * heights[idx])
            
                indices_stack.append(right)

        return max_rectangle