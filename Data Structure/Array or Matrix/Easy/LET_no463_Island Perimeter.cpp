class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int count = 0, repeat = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j]) {
                    count++;
                    if (i > 0 && grid[i - 1][j]) repeat++;
                    if (j > 0 && grid[i][j - 1]) repeat++;
                }
            }
        }
        
        return count * 4 - repeat * 2;
    }
};