class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if not (row[0] <= target <= row[-1]):
                continue
            if self.findTarget(row, target):
                return True
        
        return False
    
    def findTarget(self, row, target):
        left, right = 0, len(row)
        while left + 1 < right:
            mid = (left + right) // 2
            if row[mid] < target:
                left = mid
            else:
                right = mid
        
        if row[left] == target or row[right] == target:
            return True
        return False