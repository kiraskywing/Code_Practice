class Solution {
public:
    int numberOfArrays(string s, int k) {
        vector<int> memo(s.size(), -1);
        return dfs(s, 0, k, memo);
    }

    int dfs(string& s, int start, int limit, vector<int>& memo) {
        if (start == s.size())
            return 1;    // valid array found
        if (s[start] == '0')
            return 0;    // no leading 0
        if (memo[start] != -1)
            return memo[start];

        int res = 0;
        long num = 0;
        for (int j = start; j < s.size(); j++) {
            num = num * 10 + s[j] - '0';
            if (num > limit)
                break;
            
            res = (res + dfs(s, j + 1, limit, memo)) % (1000000007);
        }
        
        memo[start] = res;
        return res;
    }
};