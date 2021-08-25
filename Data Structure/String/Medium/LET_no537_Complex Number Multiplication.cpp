class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        int r1, i1, r2, i2;
        char buff;
        stringstream a(num1), b(num2), res;
        a >> r1 >> buff >> i1 >> buff;
        b >> r2 >> buff >> i2 >> buff;
        res << r1 * r2 - i1 * i2 << '+' << r1 * i2 + r2 * i1 << 'i';
        return res.str();
    }
};