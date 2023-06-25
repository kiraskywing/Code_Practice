class Solution {
public:
    int maxLength(vector<int>& ribbons, int k) {
        int min_val = 1, max_val = *max_element(ribbons.begin(), ribbons.end());
        while (min_val + 1 < max_val) {
            int mid_val = min_val + (max_val - min_val) / 2;
            
            if (getPieces(ribbons, mid_val) >= k)
                min_val = mid_val;
            else
                max_val = mid_val;
        }

        if (getPieces(ribbons, max_val) >= k)
            return max_val;
        if (getPieces(ribbons, min_val) >= k)
            return min_val;
        return 0;
    }

    int getPieces(vector<int>& ribbons, int length) {
        int pieces = 0;
        for (int l : ribbons)
            pieces += l / length;
        return pieces;
    }
};