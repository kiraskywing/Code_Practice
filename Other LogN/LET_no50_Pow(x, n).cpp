class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0)
            x = 1 / x;

        long times = labs(n);

        double res = 1, base = x;

        while (times > 0) {
            if (times % 2 != 0)
                res *= base;

            base *= base;
            times /= 2;
        }

        return res;
    }
};