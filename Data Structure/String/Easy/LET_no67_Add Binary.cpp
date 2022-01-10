class Solution {
public:
    string addBinary(string a, string b) {
        int n1 = a.size(), n2 = b.size();
        int n = max(n1, n2) + 1;
        string res(n, '0');
        int i = n1 - 1, j = n2 - 1, k = n - 1, cur = 0;
        while (i >= 0 || j >= 0) {
            if (i >= 0)
                cur += a[i--] - '0';
            if (j >= 0)
                cur += b[j--] - '0';
            res[k--] = '0' + cur % 2;
            cur /= 2;
        }
        res[k] = '0' + cur % 2;
        return res[0] == '0' ? res.substr(1) : res;
    }
};