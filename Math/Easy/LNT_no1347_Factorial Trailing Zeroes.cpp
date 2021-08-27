class Solution {
public:
    /**
     * @param n: a integer
     * @return: return a integer
     */
    int trailingZeroes(int n) {
        // write your code here
        int res = 0;
        while (n >= 5) {
            res += n / 5;
            n /= 5;
        }
        return res;
    }
};