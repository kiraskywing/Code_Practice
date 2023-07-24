class Solution {
private:
    int n;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        n = s.size();
        unordered_set<string> dict(wordDict.begin(), wordDict.end());
        unordered_map<int, vector<string>> memo;
        return helper(s, 0, dict, memo);
    }

    vector<string> helper(string& s, int i, unordered_set<string>& dict, unordered_map<int, vector<string>>& memo) {
        if (i == n)
            return {};
        if (memo.count(i))
            return memo[i];

        vector<string> res;
        string s2;
        for (int j = i + 1; j <= n; j++) {
            s2 = s.substr(i, j - i);
            if (!dict.count(s2))
                continue;

            for (string& sub : helper(s, j, dict, memo))
                res.push_back(s2 + " " + sub);
        }

        s2 = s.substr(i);
        if (dict.count(s2))
            res.push_back(s2);
        memo[i] = res;

        return res;
    }
};