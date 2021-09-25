class Solution {
public:
    int shortestPath(vector<vector<int>> &grid, int k) {
        const int dx[] = {-1, 0, 0, 1}, dy[] = {0, -1, 1, 0};
        int m = grid.size(), n = grid[0].size(), step = 0;
        vector<vector<int>> remains(m, vector<int>(n, INT_MIN));
        vector<vector<int>> shifts = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        queue<vector<int>> q;
        q.push({0, 0, k}), remains[0][0] = k;
        
        while (!q.empty()) {
            for (int k = q.size(); k > 0; k--) {
                auto cur = q.front();
                int i = cur[0], j = cur[1], lefts = cur[2];
                q.pop();
                if (i == m - 1 && j == n - 1) 
                    return step;
                
                for (auto& s : shifts) {
                    int x = i + s[0], y = j + s[1];
                    if (0 <= x && x < m && 0 <= y && y < n) {
                        int re = lefts - grid[x][y];
                        if (re >= 0 && re > remains[x][y]) {
                            q.push({x, y, re});
                            remains[x][y] = re;
                        }    
                    }
                }
            }
            step++;
        }
        return -1;
    }
};