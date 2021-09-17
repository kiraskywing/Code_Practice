class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        int i = 0, j = 0, di = 0, dj = 1, times = m * n;
        vector<int> res;
        
        while (times--) {
            res.push_back(matrix[i][j]);
            matrix[i][j] = -1000;
            if (matrix[(m + i + di) % m][(n + j + dj) % n] == -1000) {
                int temp = dj;
                dj = -di;
                di = temp;
            }
            i += di; j += dj;
        }
        
        return res;
    }
};