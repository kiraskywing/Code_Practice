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

        start, end = 0, y
        while start + 1 < end:
            mid = (start + end) // 2
            if self.col_has_pixel(image, mid, 0, m - 1):
                end = mid
            else:
                start = mid
        if self.col_has_pixel(image, start, 0, m - 1):
            left = start
        elif self.col_has_pixel(image, end, 0, m - 1):
            left = end

        start, end = y, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.col_has_pixel(image, mid, 0, m - 1):
                start = mid
            else:
                end = mid
        if self.col_has_pixel(image, end, 0, m - 1):
            right = end
        elif self.col_has_pixel(image, start, 0, m - 1):
            right = start

        start, end = 0, x
        while start + 1 < end:
            mid = (start + end) // 2
            if self.row_has_pixel(image, mid, 0, n - 1):
                end = mid
            else:
                start = mid
        if self.row_has_pixel(image, start, 0, n - 1):
            down = start
        elif self.row_has_pixel(image, end, 0, n - 1):
            down = end

        start, end = x, m - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.row_has_pixel(image, mid, 0, n - 1):
                start = mid
            else:
                end = mid
        if self.row_has_pixel(image, end, 0, n - 1):
            up = end
        elif self.row_has_pixel(image, start, 0, n - 1):
            up = start

        return (right - left + 1) * (up - down + 1)

    def col_has_pixel(self, matrix, index, top, bottom):
        if top == bottom:
            return matrix[top][index] == "1"

        mid = (top + bottom) // 2
        return self.col_has_pixel(matrix, index, top, mid) or self.col_has_pixel(matrix, index, mid + 1, bottom)

    def row_has_pixel(self, matrix, index, left, right):
        if left == right:
            return matrix[index][left] == "1"

        mid = (left + right) // 2
        return self.row_has_pixel(matrix, index, left, mid) or self.row_has_pixel(matrix, index, mid + 1, right)