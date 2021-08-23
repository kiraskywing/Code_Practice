class Solution {
public:
    int rectangleArea(vector<vector<int>>& rectangles) {
        set<int> xs, ys;
        for (auto rec : rectangles)
            xs.insert(rec[0]), ys.insert(rec[1]), xs.insert(rec[2]), ys.insert(rec[3]);
        
        unordered_map<int, int> x_i, y_j, i_x, j_y;
        int i_count = 0, j_count = 0;
        for (auto x = xs.begin(); x != xs.end(); x++) {
            x_i[*x] = i_count;
            i_x[i_count] = *x;
            i_count++;
        }
        for (auto y = ys.begin(); y != ys.end(); y++) {
            y_j[*y] = j_count;
            j_y[j_count] = *y;
            j_count++;
        }
        
        vector<vector<int>> board(i_count, vector<int>(j_count, 0));
        for (auto rec : rectangles) {
            int i1 = x_i[rec[0]], j1 = y_j[rec[1]], i2 = x_i[rec[2]], j2 = y_j[rec[3]];
            for (int i = i1; i < i2; i++) {
                for (int j = j1; j < j2; j++)
                    board[i][j] = 1;
            }
        }
        
        long long res = 0;
        int mod = (int) (1e9 + 7);
        for (int i = 0; i < i_count; i++) {
            for (int j = 0; j < j_count; j++) {
                if (board[i][j]) {
                    res += ((long long)(i_x[i + 1] - i_x[i])) * (j_y[j + 1] - j_y[j]);
                    res %= mod;
                }
            }
        }
        
        return res;
    }
};