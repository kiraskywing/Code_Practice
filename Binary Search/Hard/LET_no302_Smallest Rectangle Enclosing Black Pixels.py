class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        up = self.get_row_bound(image, 0, x, True)
        down = self.get_row_bound(image, x + 1, len(image) - 1, False)
        left = self.get_col_bound(image, 0, y, True)
        right = self.get_col_bound(image, y + 1, len(image[0]) - 1, False)
        return (down - up) * (right - left)

    def get_row_bound(self, image, start, end, find_one):
        if start > end:
            return end + 1
        
        while start + 1 < end:
            mid = (start + end) // 2
            if any('1' == pixel for pixel in image[mid]) == find_one:
                end = mid
            else:
                start = mid
        
        if any('1' == pixel for pixel in image[start]) == find_one:
            return start
        if any('1' == pixel for pixel in image[end]) == find_one:
            return end
        return end + 1

    def get_col_bound(self, image, start, end, find_one):
        if start > end:
            return end + 1
        m = len(image)
        while start + 1 < end:
            mid = (start + end) // 2
            if any('1' == image[i][mid] for i in range(m)) == find_one:
                end = mid
            else:
                start = mid
        
        if any('1' == image[i][start] for i in range(m)) == find_one:
            return start
        if any('1' == image[i][end] for i in range(m)) == find_one:
            return end
        return end + 1
