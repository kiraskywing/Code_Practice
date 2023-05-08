class Solution {
public:
    int diagonalSum(vector<vector<int>>& mat) {
        int res = 0;
        int m = mat.size(), n = mat[0].size();
        int j = 0, j2 = n - 1;

        for (int i = 0; i < m; i++) {
            res += (mat[i][j] + mat[i][j2]);
            if (j == j2)
                res -= mat[i][j];
            j++;
            j2--;
        }

        return res;
    }
};