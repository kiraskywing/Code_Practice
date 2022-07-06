class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.nums = [[0] * n for _ in range(m)]
        self.bit = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.nums[row][col]
        self.nums[row][col] = val
        
        i = row + 1
        while i <= len(self.nums):
            j = col + 1
            while j <= len(self.nums[row]):
                self.bit[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.query(row2, col2) - self.query(row2, col1 - 1) - self.query(row1 - 1, col2) + self.query(row1 - 1, col1 - 1)

    def query(self, row, col):
        res = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                res += self.bit[i][j]
                j -= (j & -j)
            i -= (i & -i)
        return res
    
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)