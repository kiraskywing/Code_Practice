class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """

    def minArea(self, image, x, y):
        m = len(image)
        if m == 0:
            return 0
        n = len(image[0])
        if n == 0:
            return 0

        boundaries = [x, x, y, y]
        visited = {(x, y)}
        queue = [(x, y)]

        for i, j in queue:
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1)]:
                i2, j2 = i + di, j + dj
                if 0 <= i2 < m and 0 <= j2 < n and image[i2][j2] == "1" and (i2, j2) not in visited:
                    visited.add((i2, j2))
                    self.update_boundaries(boundaries, i2, j2)
                    queue.append([i2, j2])

        length = boundaries[1] - boundaries[0] + 1
        width = boundaries[3] - boundaries[2] + 1
        return length * width

    def update_boundaries(self, boundaries, x, y):
        boundaries[0] = min(boundaries[0], x)
        boundaries[1] = max(boundaries[1], x)
        boundaries[2] = min(boundaries[2], y)
        boundaries[3] = max(boundaries[3], y)

