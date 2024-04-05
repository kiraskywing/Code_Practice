class Solution {
public:
    string makeGood(string s) {
        int n = s.size(), i = 0;
        string res = "";
        while (i < n) {
            if (!res.empty() && res.back() != s[i] && tolower(res.back()) == tolower(s[i])) {
                res.pop_back();
                i++;
                continue;
            }

            res.push_back(s[i++]);
        }

        return res;
    }
};