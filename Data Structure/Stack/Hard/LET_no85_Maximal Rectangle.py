class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * (n + 1)
        heights[-1] = -1
        
        res = 0
        for row in matrix:
            stack = []
            for right in range(n + 1):
                if right < n:
                    heights[right] = heights[right] + 1 if row[right] == '1' else 0
                    
                while stack and heights[stack[-1]] > heights[right]:
                    idx = stack.pop()
                    h = heights[idx]
                    left = stack[-1] if stack else -1
                    res = max(res, (right - left - 1) * h)
                
                stack.append(right)
        
        return res