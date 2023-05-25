class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int m = matrix.size(), n = matrix[0].size();
        int left = 0, right = m * n - 1;

        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            int i = mid / n, j = mid % n;
            if (matrix[i][j] >= target)
                right = mid;
            else 
                left = mid;
        }

        if (matrix[left / n][left % n] == target)
            return true;
        if (matrix[right / n][right % n] == target)
            return true;
        return false;
    }
};