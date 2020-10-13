class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.arr = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.bit = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]

        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        delta = val - self.arr[row][col]
        self.arr[row][col] = val

        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += delta
                j += self.lowbit(j)
            i += self.lowbit(i)

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.prefix_sum(row2, col2) - self.prefix_sum(row1 - 1, col2) - self.prefix_sum(row2, col1 - 1) + self.prefix_sum(
            row1 - 1, col1 - 1)

    def prefix_sum(self, row, col):
        result = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                result += self.bit[i][j]
                j -= self.lowbit(j)
            i -= self.lowbit(i)
        return result

    def lowbit(self, index):
        return index & -index

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)