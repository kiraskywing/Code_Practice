class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        n = len(colors)
        right_most = [0] * 3
        left_most = [n - 1] * 3
        dist = [[-1] * n for _ in range(3)]
        
        for i in range(n):
            color = colors[i] - 1
            for j in range(right_most[color], i + 1):
                dist[color][j] = i - j
            right_most[color] = i + 1
        
        for i in range(n - 1, -1, -1):
            color = colors[i] - 1
            for j in range(left_most[color], i - 1, -1):
                if dist[color][j] == -1 or j - i < dist[color][j]:
                    dist[color][j] = j - i
            left_most[color] = i - 1
        
        res = []
        for i, color in queries:
            res.append(dist[color - 1][i])
        return res