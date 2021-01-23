class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        record = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                record[i - j].append(mat[i][j])
        
        for key in record:
            record[key].sort(reverse=True)
        
        for i in range(m):
            for j in range(n):
                mat[i][j] = record[i - j].pop()
        return mat