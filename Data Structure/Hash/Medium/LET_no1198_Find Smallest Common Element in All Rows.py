class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        memo = collections.defaultdict(int)
        for row in mat:
            for num in row:
                memo[num] += 1
                if memo[num] == m:
                    return num
        
        return -1