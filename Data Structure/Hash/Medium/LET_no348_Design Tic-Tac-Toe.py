class TicTacToe:

    def __init__(self, n: int):
        self.count = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.plus = 0
        self.minus = 0

    def move(self, row: int, col: int, player: int) -> int:
        offset = player * 2 - 3
        self.rows[row] += offset
        self.cols[col] += offset
        if row + col == self.count - 1:
            self.plus += offset
        if row - col == 0:
            self.minus += offset
            
        if self.count in (self.rows[row], self.cols[col], self.plus, self.minus):
            return 2
        if -self.count in (self.rows[row], self.cols[col], self.plus, self.minus):
            return 1
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)