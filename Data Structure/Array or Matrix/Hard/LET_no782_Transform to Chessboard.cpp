class Solution {
public:
    int movesToChessboard(vector<vector<int>>& board) {
        int n = board.size();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (board[0][0] ^ board[0][j] ^ board[i][0] ^ board[i][j])
                    return -1;
            }
        }
        
        int rowSum = 0, colSum = 0, rMissPlace = 0, cMissPlace = 0;
        for (int i = 0; i < n; i++) {
            rowSum += board[i][0];
            colSum += board[0][i];
            rMissPlace += board[i][0] == i % 2;
            cMissPlace += board[0][i] == i % 2;
        }
        
        if (rowSum != n / 2 && rowSum != (n + 1) / 2 || colSum != n / 2 && colSum != (n + 1) / 2)
            return -1;
        
        if (n % 2) {
            if (rMissPlace % 2) rMissPlace = n - rMissPlace;
            if (cMissPlace % 2) cMissPlace = n - cMissPlace;
        }
        else {
            rMissPlace = min(rMissPlace, n - rMissPlace);
            cMissPlace = min(cMissPlace, n - cMissPlace);
        }
        
        return (rMissPlace + cMissPlace) / 2;
    }
};