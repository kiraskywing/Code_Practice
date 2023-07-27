class Solution {
private:
    int m, n;
public:
    bool isMatch(string s, string p) {
        unordered_map<int, bool> memo;
        m = s.size();
        n = p.size();
        return helper(s, 0, p, 0, memo);
    }

    bool helper(string& s, int i, string& p, int j, unordered_map<int, bool>& memo) {
        int key = i * n + j;
        if (memo.count(key))
            return memo[key];
        
        if (i == m)
            return isValid(p, j);
        if (j == n)
            return false;

        bool res = false;
        if (j + 1 < n && p[j + 1] == '*')
            res = isMatch(s[i], p[j]) && helper(s, i + 1, p, j, memo) || helper(s, i, p, j + 2, memo);
        else 
            res = isMatch(s[i], p[j]) && helper(s, i + 1, p, j + 1, memo);

        memo[key] = res;
        return res;
    }

    bool isValid(string& s, int start) {
        if ((n - start) % 2)
            return false;
        
        for (int i = start + 1; i < n; i += 2) {
            if (s[i] != '*')
                return false;
        }
            
        return true;
    }

    bool isMatch(char a, char b) {
        return a == b || b == '.';
    }
};