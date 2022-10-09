class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        memo = collections.defaultdict(list)
        i, di = 0, 1
        for c in s:
            memo[i].append(c)
            if not (0 <= i + di < numRows):
                di = -di
            i += di
        
        return ''.join(c for i in range(numRows) for c in memo[i])