class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int res = -1;
        unordered_map<char, vector<int>> memo;
        for (int i = 0; i < s.size(); i++) {
            if (memo.count(s[i]))
                res = max(res, i - memo[s[i]].back() - 1);
            else
                memo[s[i]].push_back(i);
        }

        return res;
    }
};