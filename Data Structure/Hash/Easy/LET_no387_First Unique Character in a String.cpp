class Solution {
public:
    int firstUniqChar(string s) {
        unordered_map<char, int> memo;
        for (char c : s)
            memo[c] += 1;

        for (int i = 0; i < s.size(); i++) {
            if (memo[s[i]] == 1)
                return i;
        }

        return -1;
    }
};