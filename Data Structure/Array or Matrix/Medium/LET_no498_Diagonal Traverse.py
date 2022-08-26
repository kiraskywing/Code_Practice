class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        memo = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                memo[i + j].append(mat[i][j])
                
        res = []
        for key in range(m + n - 1):
            if key % 2 == 0:
                res.extend(reversed(memo[key]))
            else:
                res.extend(memo[key])
        
        return res