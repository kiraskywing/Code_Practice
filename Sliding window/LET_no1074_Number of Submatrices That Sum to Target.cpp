class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size(), res = 0;
        for (auto &row : matrix)
            for (int j = 0; j < n - 1; j++)
                row[j + 1] += row[j];
        
        unordered_map<int, int> counter;
        for (int j1 = 0; j1 < n; j1++) {
            for (int j2 = j1; j2 < n; j2++) {
                counter = {{0, 1}};
                int cur = 0;
                for (int i = 0; i < m; i++) {
                    cur += matrix[i][j2] - (j1 > 0 ? matrix[i][j1 - 1] : 0);
                    res += counter.find(cur - target) != counter.end() ? counter[cur - target] : 0;
                    counter[cur]++;
                }
            }
        }
        
        return res;
    }
};