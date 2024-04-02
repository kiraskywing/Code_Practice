class Solution {
public:
    bool isIsomorphic(string s, string t) {
        unordered_map<char, char> memo;
        unordered_set<char> used;
        for (int i = 0; i < s.size(); i++) {
            char c1 = s[i], c2 = t[i];
            if (!memo.count(c1)) {
                if (used.count(c2))
                    return false;
                memo[c1] = c2;
                used.insert(c2);
            }
            else if (memo[c1] != c2)
                return false;
        }

        return true;
    }
};