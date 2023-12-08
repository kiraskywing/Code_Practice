class Solution {
public:
    int totalNQueens(int n) {
        // 0: col, 1: row + col, 2: row - col
        vector<unordered_set<int>> memo(3, unordered_set<int>());
        return helper(0, n, memo);
    }

    int helper(int row, int n, vector<unordered_set<int>>& memo) {
        if (row == n)
            return 1;

        int cur = 0;
        for (int col = 0; col < n; col++) {
            if (isValid(row, col, memo)) {
                memo[0].insert(col);
                memo[1].insert(row + col);
                memo[2].insert(row - col);
                cur += helper(row + 1, n, memo);
                memo[0].erase(col);
                memo[1].erase(row + col);
                memo[2].erase(row - col);
            }
        }
        return cur;
    }

    bool isValid(int row, int col, vector<unordered_set<int>>& memo) {
        return !(memo[0].count(col) || memo[1].count(row + col) || memo[2].count(row - col));
    }
};