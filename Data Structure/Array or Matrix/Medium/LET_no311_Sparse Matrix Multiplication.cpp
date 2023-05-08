class Solution {
public:
    vector<vector<int>> multiply(vector<vector<int>>& mat1, vector<vector<int>>& mat2) {
        int m = mat1.size(), n = mat2[0].size();
        vector<vector<vector<int>>> rows(m, vector<vector<int>>());
        vector<vector<vector<int>>> cols(n, vector<vector<int>>());
        vector<vector<int>> res(m, vector<int>(n, 0));

        for (int i = 0; i < mat1.size(); i++) {
            for (int j = 0; j < mat1[0].size(); j++) {
                if (mat1[i][j] != 0)
                    rows[i].push_back({j, mat1[i][j]});
            }
        }

        for (int i = 0; i < mat2.size(); i++) {
            for (int j = 0; j < mat2[0].size(); j++) {
                if (mat2[i][j] != 0)
                    cols[j].push_back({i, mat2[i][j]});
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++)
                res[i][j] = product(rows[i], cols[j]);
        }

        return res;
    }

    int product(vector<vector<int>>& row, vector<vector<int>>& col) {
        int i = 0, j = 0, res = 0;
        while (i < row.size() && j < col.size()) {
            if (row[i][0] < col[j][0])
                i++;
            else if (row[i][0] > col[j][0])
                j++;
            else {
                res += row[i][1] * col[j][1];
                i++;
                j++;
            }
                
        }

        return res;
    }
};