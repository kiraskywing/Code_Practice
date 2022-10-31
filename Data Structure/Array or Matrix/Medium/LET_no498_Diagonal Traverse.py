class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        memo = collections.defaultdict(list)
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                memo[i + j].append(mat[i][j])
                
        res = []
        for key in memo:
            if key % 2 == 0:
                res.extend(reversed(memo[key]))
            else:
                res.extend(memo[key])
        
        return res

class Solution2:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        res = []
        for k in range(m + n - 1):
            if k % 2 == 0:
                i = min(m - 1, k)
                j = k - i
                di, dj = -1, 1
            else:
                j = min(n - 1, k)
                i = k - j
                di, dj = 1, -1
            
            while 0 <= i < m and 0 <= j < n:
                res.append(mat[i][j])
                i, j = i + di, j + dj
        
        return res

"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output1: [1,2,4,7,5,3,6,8,9]
Output2: [1,4,2,7,5,3,8,6,9]

| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |

Example 2:
Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]

| 1 | 2 |
---------
| 3 | 4 |
"""