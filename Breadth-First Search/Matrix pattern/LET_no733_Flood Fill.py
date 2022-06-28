class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color == color:
            return image
        
        queue = collections.deque([(sr, sc)])
        image[sr][sc] = color
        
        while queue:
            i, j = queue.popleft()
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and image[i2][j2] == start_color:
                    image[i2][j2] = color
                    queue.append((i2, j2))
        
        return image