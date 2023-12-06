class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        auto p = toRemove(s);
        int lefts = p.first, rights = p.second;
        vector<string> temp, res;
        helper(s, 0, lefts, rights, temp, res);
        return res;
    }

    pair<int, int> toRemove(string& s) {
        int lefts = 0, rights = 0;
        for (char c: s) {
            if (c == '(')
                lefts++;
            else if (c == ')') {
                if (lefts > 0)
                    lefts--;
                else
                    rights++;
            }
        }

        return {lefts, rights};
    }

    void helper(string& s, int start, int lefts, int rights, vector<string>& temp, vector<string>& res) {
        if (lefts == 0 && rights == 0) {
            string cur = "";
            for (string& sub : temp)
                cur += sub;
            cur += s.substr(start);
            if (isValid(cur))
                res.push_back(cur);
            return;
        }

        if (lefts < 0 || rights < 0)
            return;

        for (int end = start; end < s.size(); end++) {
            if (end > start && s[end] == s[end - 1])
                continue;

            if (s[end] == '(') {
                temp.push_back(s.substr(start, end - start));
                helper(s, end + 1, lefts - 1, rights, temp, res);
                temp.pop_back();
            }
            else if (s[end] == ')') {
                temp.push_back(s.substr(start, end - start));
                helper(s, end + 1, lefts, rights - 1, temp, res);
                temp.pop_back();
            }
        }
    }

    bool isValid(string& s) {
        auto p = toRemove(s);
        return p.first == 0 && p.second == 0;
    }
};