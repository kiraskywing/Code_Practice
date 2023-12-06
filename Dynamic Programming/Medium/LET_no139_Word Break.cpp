class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        int max_len = -1;
        for (string& s: wordDict)
            max_len = int(s.size()) > max_len ? int(s.size()) : max_len;
        unordered_map<int, bool> memo;
        return helper(s, 0, max_len, dict, memo);
    }

    bool helper(string& s, int start, int max_len, unordered_set<string>& dict, unordered_map<int, bool>& memo) {
        if (start == s.size())
            return true;

        if (!memo.count(start)) {
            bool res = false;
            for (int length = 1; length <= min(max_len, int(s.size()) - start); length++) {
                string sub = s.substr(start, length);
                if (dict.count(sub) && helper(s, start + length, max_len, dict, memo))
                    res = true;
            }
            memo[start] = res;
        }

        return memo[start];
    }
};