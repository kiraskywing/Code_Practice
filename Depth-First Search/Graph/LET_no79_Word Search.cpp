class Solution {
private:
    int m, n;
public:
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size(), n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (helper(board, i, j, word, 0))
                    return true;
            }
        }
        return false;
    }
    
    bool helper(vector<vector<char>>& board, int i, int j, string& word, int k) {
        if (!validPos(board, i, j) || board[i][j] != word[k])
            return false;
        if (k == word.size() - 1)
            return true;
        
        board[i][j] = '*';
        bool res = helper(board, i - 1, j, word, k + 1)
                || helper(board, i + 1, j, word, k + 1)
                || helper(board, i, j + 1, word, k + 1)
                || helper(board, i, j - 1, word, k + 1);
        board[i][j] = word[k];
        
        return res;
    }
    
    bool validPos(vector<vector<char>>& board, int i, int j) {
        return 0 <= i && i < m && 0 <= j && j < n;
    }
};