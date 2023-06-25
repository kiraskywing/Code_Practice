class Solution {
public:
    int mySqrt(int x) {
        long low = 0, high = x;
        while (low + 1 < high) {
            long mid = low + (high - low) / 2;
            if (mid * mid > x)
                high = mid;
            else
                low = mid;
        }

        if (high * high <= x)
            return high;
        return low;
    }
};