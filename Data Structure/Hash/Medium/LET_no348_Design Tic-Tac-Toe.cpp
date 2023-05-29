class TicTacToe {
private:
    int diagonal, diagonalInv, count;
    vector<int> rows, cols;
public:
    TicTacToe(int n) {
        count = n;
        diagonal = diagonalInv = 0;
        rows.resize(n, 0);
        cols.resize(n, 0);
    }
    
    int move(int row, int col, int player) {
        int offset = player * 2 - 3;    // player1: -1, player2: 1
        rows[row] += offset;
        cols[col] += offset;
        if (row == col)
            diagonal += offset;
        if (row + col == count - 1)
            diagonalInv += offset;

        if (rows[row] == count || cols[col] == count || diagonal == count || diagonalInv == count)
            return 2;
        if (rows[row] == -count || cols[col] == -count || diagonal == -count || diagonalInv == -count)
            return 1;
        return 0;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */