# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        res = n
        for i in range(m):
            res = min(res, self.getFirstOneIndex(binaryMatrix, i, 0, n - 1))
        return res if res != n else -1
    
    def getFirstOneIndex(self, arr, i, left_j, right_j):
        while left_j + 1 < right_j:
            mid_j = (left_j + right_j) // 2
            if arr.get(i, mid_j) == 0:
                left_j = mid_j
            else:
                right_j = mid_j
        
        if arr.get(i, left_j) == 1:
            return left_j
        if arr.get(i, right_j) == 1:
            return right_j
        return float('inf')

class Solution2:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        i, j = 0, n - 1
        while i < m and j >= 0:
            if binaryMatrix.get(i, j) == 1:
                j -= 1
            else:
                i += 1
        return j + 1 if j != n - 1 else -1