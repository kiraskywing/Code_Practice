class Solution {
private:
    int rows[9][9], cols[9][9], blocks[9][9];
public:
    void solveSudoku(vector<vector<char>>& board) {
        memset(rows, 0, sizeof(rows));
        memset(cols, 0, sizeof(cols));
        memset(blocks, 0, sizeof(blocks));
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int num = board[i][j] - '1', k = i / 3 * 3 + j / 3;
                    rows[i][num] = cols[j][num] = blocks[k][num] = 1;
                }
            }
        }
        
        solver(board, 0, 0);
    }
    bool solver(vector<vector<char>>& board, int i, int j) {
        if (i == 9)
            return true;
        if (j == 9)
            return solver(board, i + 1, 0);
        if (board[i][j] != '.')
            return solver(board, i, j + 1);
        
        int k = i / 3 * 3 + j / 3;
        for (char c = '1'; c <= '9'; c++) {
            int num = c - '1';
            if (check(i, j, k, num)) {
                board[i][j] = c;
                rows[i][num] = cols[j][num] = blocks[k][num] = 1;
                if (solver(board, i, j+ 1))
                    return true;
                rows[i][num] = cols[j][num] = blocks[k][num] = 0;
                board[i][j] = '.';
            }
        }
        
        return false;
    }
    bool check(int i, int j, int k, int num) {
        if (rows[i][num] || cols[j][num] || blocks[k][num])
            return false;
        return true;
    }
};