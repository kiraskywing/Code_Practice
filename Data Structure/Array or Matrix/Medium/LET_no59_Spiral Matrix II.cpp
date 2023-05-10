class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> res(n, vector<int>(n, 0));
        int val = 1, i = 0, j = 0, di = 0, dj = 1;
        while (val <= n * n) {
            res[i][j] = val;
            int i2 = (i + di + n) % n, j2 = (j + dj + n) % n;
            if (res[i2][j2] != 0) {
                int temp = dj;
                dj = -di, di = temp;
            }
            i += di;
            j += dj;
            val++;
        }

        return res;
    }
};