class Solution {
private:
    int m, n;
public:
    int minArea(vector<vector<char>>& image, int x, int y) {
        m = image.size();
        n = image[0].size();
        int upper_row = searchRow(image, 0, x, true);
        int lower_row = searchRow(image, x + 1, m - 1, false);
        int left_col = searchCol(image, 0, y, true);
        int right_col = searchCol(image, y + 1, n - 1, false);
        return (lower_row - upper_row) * (right_col - left_col);
    }

    int searchRow(vector<vector<char>>& image, int up_row, int low_row, bool has_pixel) {
        if (up_row > low_row)
            return low_row + 1;

        while (up_row + 1 < low_row) {
            int mid_row = up_row + (low_row - up_row) / 2;
            if (rowHasPixel(image, mid_row) == has_pixel)
                low_row = mid_row;
            else
                up_row = mid_row;

        }
        
        if (rowHasPixel(image, up_row) == has_pixel)
            return up_row;
        if (rowHasPixel(image, low_row) == has_pixel)
            return low_row;
        return low_row + 1;
    }

    int searchCol(vector<vector<char>>& image, int left_col, int right_col, bool has_pixel) {
        if (left_col > right_col)
            return right_col + 1;
        
        while (left_col + 1 < right_col) {
            int mid_col = left_col + (right_col - left_col) / 2;
            if (colHasPixel(image, mid_col) == has_pixel)
                right_col = mid_col;
            else
                left_col = mid_col;
        }

        if (colHasPixel(image, left_col) == has_pixel)
            return left_col;
        if (colHasPixel(image, right_col) == has_pixel)
            return right_col;
        return right_col + 1;
    }

    bool rowHasPixel(vector<vector<char>>& image, int row) {
        bool has_pixel = false;
        for (int j = 0; j < n && has_pixel == false; j++)
            has_pixel |= image[row][j] == '1';
        return has_pixel;
    }

    bool colHasPixel(vector<vector<char>>& image, int col) {
        bool has_pixel = false;
        for (int i = 0; i < m && has_pixel == false; i++)
            has_pixel |= image[i][col] == '1';
        return has_pixel;
    }
};