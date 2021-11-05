class Solution {
public:
    int arrangeCoins(int n) {
        long low = 1, high = n, mid, cur;
        while (low + 1 < high) {
            mid = (low + high) / 2;
            cur = mid * (mid + 1) / 2;
            if (cur <= n)
                low = mid;
            else
                high = mid;
        }
        
        cur = high * (high + 1) / 2;
        if (cur <= n)
            return high;
        return low;
    }
};