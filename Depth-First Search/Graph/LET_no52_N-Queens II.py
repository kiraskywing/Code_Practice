class Solution:
    def totalNQueens(self, n: int) -> int:
        memo = {'col':set(), 'minus':set(), 'add':set()}
        return self.helper(0, n, memo)

    def helper(self, row, n, memo):
        if row == n:
            return 1

        cur = 0
        for col in range(n):
            if self.is_valid(row, col, memo):
                memo['col'].add(col)
                memo['minus'].add(row - col)
                memo['add'].add(row + col)
                cur += self.helper(row + 1, n, memo)
                memo['col'].remove(col)
                memo['minus'].remove(row - col)
                memo['add'].remove(row + col)
        return cur

    def is_valid(self, row, col, memo):
        if col in memo['col'] or (row - col) in memo['minus'] or (row + col) in memo['add']:
            return False
        return True