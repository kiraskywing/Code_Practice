class Solution {
public:
    vector<vector<string>> solveNQueens(int n) {
        vector<vector<string>> res;
        vector<int> cols;
        // 0: cols, 1: row + col, 2: row - col
        vector<unordered_set<int>> memo(3, unordered_set<int>());
        helper(n, cols, memo, res);
        return res;
    }

    void helper(int n, vector<int>& cols, vector<unordered_set<int>>& memo, vector<vector<string>>& res) {
        int row = cols.size();
        if (row == n) {
            res.push_back(draw(cols));
            return;
        }

        for (int col = 0; col < n; col++) {
            if (isValid(row, col, memo)) {
                memo[0].insert(col);
                memo[1].insert(row + col);
                memo[2].insert(row - col);
                cols.push_back(col);
                helper(n, cols, memo, res);
                cols.pop_back();
                memo[0].erase(col);
                memo[1].erase(row + col);
                memo[2].erase(row - col);
            }
        }
    }

    bool isValid(int row, int col, vector<unordered_set<int>>& memo) {
        return !(memo[0].count(col) || memo[1].count(row + col) || memo[2].count(row - col));
    }

    vector<string> draw(vector<int>& cols) {
        int n = cols.size();
        vector<string> res;
        for (int col : cols) {
            string row(n, '.');
            row[col] = 'Q';
            res.push_back(row);
        }
        return res;
    }
};