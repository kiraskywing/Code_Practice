class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        r_low, r_high = 0, len(mat) - 1
        while r_low <= r_high:
            r_mid = (r_low + r_high) // 2
            c = self.findPeakCol(mat[r_mid])
            
            left_is_big = r_mid - 1 >= r_low and mat[r_mid - 1][c] > mat[r_mid][c]
            right_is_big = r_mid + 1 <= r_high and mat[r_mid + 1][c] > mat[r_mid][c]
            
            if not left_is_big and not right_is_big:
                return [r_mid, c]
            elif left_is_big:
                r_high = r_mid - 1
            else:
                r_low = r_mid + 1
                
        return [-1, -1]
    
    def findPeakCol(self, arr):
        col = 0
        for i in range(len(arr)):
            if arr[i] > arr[col]:
                col = i
        return col