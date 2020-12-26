class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        rec = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                rec[i + j].append(matrix[i][j])
        
        res = []
        for key in sorted(rec):
            if key % 2 == 0:
                res.extend(reversed(rec[key]))
            else:
                res.extend(rec[key])
        
        return res