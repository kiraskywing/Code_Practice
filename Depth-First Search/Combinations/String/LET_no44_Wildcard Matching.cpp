class Solution {
private:
    int m, n;
public:
    bool isMatch(string s, string p) {
        m = s.size();
        n = p.size();
        unordered_map<int, bool> memo;
        return helper(s, 0, p, 0, memo);
    }

    bool helper(string& s, int i, string& p, int j, unordered_map<int, bool>& memo) {
        int key = i * n + j;
        if (memo.count(key))
            return memo[key];
        
        if (i == m) {
            if (j == n)
                return true;
            else {
                while (j < n && p[j] == '*')
                    j++;
                return j == n;
            }
        }

        if (j == n)
            return false;

        bool matched;
        if (p[j] != '*')
            matched = (s[i] == p[j] || p[j] == '?') && helper(s, i + 1, p, j + 1, memo);
        else
            matched = helper(s, i, p, j + 1, memo) || helper(s, i + 1, p, j, memo);

        memo[key] = matched;
        return matched;
    }
};