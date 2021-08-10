class Solution {
public:
    string addStrings(string num1, string num2) {
        int i = num1.size() - 1;
        int j = num2.size() - 1;
        int nxt = 0;
        string res = "";
        
        while (i >= 0 || j >= 0) {
            int cur = nxt;
            if (i >= 0) {
                cur += num1[i] - '0';
                i--;
            }
            if (j >= 0) {
                cur += num2[j] - '0';
                j--;
            }
            res += to_string(cur % 10);
            nxt = cur / 10;
        }
        
        if (nxt)
            res += '1';
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};