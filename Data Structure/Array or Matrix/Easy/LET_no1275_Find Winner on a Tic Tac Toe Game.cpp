class Solution {
public:
    string tictactoe(vector<vector<int>>& moves) {
        vector<vector<int>> row(2, vector<int>(3, 0)), col(2, vector<int>(3, 0)), di(2, vector<int>(2, 0));
        int player = 0;
        for (int i = 0; i < moves.size(); i++) {
            int r = moves[i][0], c = moves[i][1];
            row[player][r]++;
            col[player][c]++;
            di[player][0] += r == c ? 1 : 0;
            di[player][1] += r + c == 2 ? 1 : 0;
            if (row[player][r] == 3 || col[player][c] == 3 || di[player][0] == 3 || di[player][1] == 3)
                return player == 0 ? "A" : "B";
            player ^= 1;
        }
        return moves.size() == 9 ? "Draw" : "Pending";
    }
};