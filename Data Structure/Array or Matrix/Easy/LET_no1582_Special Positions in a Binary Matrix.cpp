class Solution {
public:
    int numSpecial(vector<vector<int>>& mat) {
        int m = mat.size(), n = mat[0].size();
        vector<int> rows(m, 0), cols(n, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++){
                rows[i] += mat[i][j];
                cols[j] += mat[i][j];
            }
        }

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res += (mat[i][j] && rows[i] == 1 && cols[j] == 1);
            }
        }

        return res;
    }
};