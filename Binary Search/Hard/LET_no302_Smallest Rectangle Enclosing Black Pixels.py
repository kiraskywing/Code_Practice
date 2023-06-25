class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        up_row = self.searchRows(image, 0, x, True)
        down_row = self.searchRows(image, x + 1, len(image) - 1, False)
        left_col = self.searchCols(image, 0, y, True)
        right_col = self.searchCols(image, y + 1, len(image[0]) - 1, False)
        return (down_row - up_row) * (right_col - left_col)
    
    def searchRows(self, image, up, down, condition):
        if up > down:
            return down + 1
        
        while up + 1 < down:
            mid = (up + down) // 2
            if any(c == '1' for c in image[mid]) == condition:
                down = mid
            else:
                up = mid
        if any(c == '1' for c in image[up]) == condition:
            return up
        if any(c == '1' for c in image[down]) == condition:
            return down
        return down + 1
    
    def searchCols(self, image, left, right, condition):
        if left > right:
            return right + 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            if any(image[i][mid] == '1' for i in range(len(image))) == condition:
                right = mid
            else:
                left = mid
        if any(image[i][left] == '1' for i in range(len(image))) == condition:
            return left
        if any(image[i][right] == '1' for i in range(len(image))) == condition:
            return right
        return right + 1