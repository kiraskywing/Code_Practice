class Solution {
public:
    int findKthNumber(int m, int n, int k) {
        int low = 1, high = m * n;
        while (low + 1 < high) {
            int mid = (low + high) / 2;
            if (!enough(mid, m, n, k))
                low = mid;
            else
                high = mid;
        }
        
        if (enough(low, m, n, k))
            return low;
        return high;
    }
    
    bool enough(int num, int m, int n, int k) {
        int res = 0;
        for (int i = 1; i <= m; i++) {
            res += min(num / i, n);
        }
        return res >= k;
    }
};