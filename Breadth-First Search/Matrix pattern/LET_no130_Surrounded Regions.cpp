class Solution {
public:
    void solve(vector<vector<char>>& board) {
        int m = board.size(), n = board[0].size();
        queue<pair<int, int>> q;
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O') {
                board[i][0] = '*';
                q.push({i, 0});
            }
            if (board[i][n - 1] == 'O') {
                board[i][n - 1] = '*';
                q.push({i, n - 1});
            }
        }
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O') {
                board[0][j] = '*';
                q.push({0, j});
            }
            if (board[m - 1][j] == 'O') {
                board[m - 1][j] = '*';
                q.push({m - 1, j});
            }
        }
        
        int s[4][2] = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!q.empty()) {
            auto p = q.front(); q.pop();
            for (int i = 0; i < 4; i++) {
                int x = p.first + s[i][0], y = p.second + s[i][1];
                if (0 <= x && x < m && 0 <= y && y < n && board[x][y] == 'O') {
                    board[x][y] = '*';
                    q.push({x, y});
                }
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '*')
                    board[i][j] = 'O';
                else if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }
    }
};