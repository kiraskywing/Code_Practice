class Solution {
public:
    string removeKdigits(string num, int k) {
        int n = num.size();
        if (k >= n)
            return "0";

        string res;
        for (char c : num) {
            while (k > 0 && !res.empty() && res.back() > c) {
                res.pop_back();
                k--;
            }
            res.push_back(c);
        }

        while (k > 0) {
            res.pop_back();
            k--;
        }

        int i = 0;
        while (i < res.size() && res[i] == '0')
            i++;

        return i < res.size() ? res.substr(i) : "0";
    }
};