class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        int m = matrix.size();
        if (m == 0)
            return 0;
        int n = matrix[0].size();
        vector<int> left(n, 0), right(n, n), height(n, 0);
        int res = 0;
        
        for (int i = 0; i < m; i++) {
            int curLeft = 0, curRight = n;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] == '1') {
                    left[j] = max(left[j], curLeft);
                    height[j]++;
                }
                else {
                    height[j] = left[j] = 0;
                    curLeft = j + 1;
                }
            }
            for (int j = n - 1; j >= 0; j--) {
                if (matrix[i][j] == '1') {
                    right[j] = min(right[j], curRight);
                    res = max(res, (right[j] - left[j]) * height[j]);
                }
                else {
                    right[j] = n;
                    curRight = j;
                }
            }
        }
        
        return res;
    }
};