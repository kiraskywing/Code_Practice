class Solution {
private:
    int res, m, n, x, y;
public:
    int uniquePathsIII(vector<vector<int>>& grid) {
        m = grid.size(); n = grid[0].size(); res = 0;
        int empties = 1;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    x = i; y = j;
                }
                if (grid[i][j] == 0)
                    empties += 1;
            }
        }
        
        dfs(grid, x, y, empties);
        return res;
    }
    
    void dfs(vector<vector<int>>& grid, int i, int j, int empties) {
        if (i < 0 || i >= m || j < 0 || j >= n || grid[i][j] < 0 || empties < 0)
            return;
        if (grid[i][j] == 2) {
            res += empties == 0;
            return;
        }
        
        grid[i][j] = -2;
        dfs(grid, i - 1, j, empties - 1);
        dfs(grid, i + 1, j, empties - 1);
        dfs(grid, i, j - 1, empties - 1);
        dfs(grid, i, j + 1, empties - 1);
        grid[i][j] = 0;
    }
};