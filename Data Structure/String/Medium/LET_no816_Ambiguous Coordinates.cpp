class Solution {
public:
    vector<string> ambiguousCoordinates(string s) {
        int n = s.size();
        vector<string> res;
        for (int i = 1; i < n - 2; i++) {
            vector<string> A = helper(s.substr(1, i)), B = helper(s.substr(1 + i, n - 2 -i));
            for (string &a : A)
                for (string &b : B)
                    res.push_back("(" + a + ", " + b + ")");
        }
        return res;
    }
    vector<string> helper(string s) {
        int n = s.size();
        if (n == 0 || n > 1 && s[0] == '0' && s[n - 1] == '0') return {};
        if (n > 1 && s[0] == '0') return {"0." + s.substr(1)};
        if (n == 1 || s[n - 1] == '0') return {s};
        vector<string> temp = {s};
        for (int i = 1; i < n; i++)
            temp.push_back(s.substr(0, i) + '.' + s.substr(i));
        return temp;
    }
};