class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        string res(m + n, '0');
        
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                int cur = (num1[i] - '0') * (num2[j] - '0') + (res[i + j + 1] - '0');
                res[i + j + 1] = '0' + cur % 10;
                res[i + j] += cur / 10;
            }
        }
        
        for (int i = 0; i < m + n; i++) {
            if (res[i] != '0')
                return res.substr(i);
        }
        
        return "0";
    }
};