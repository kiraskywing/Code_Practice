class Solution {
public:
    int longestPalindrome(string s) {
        unordered_map<char, int> counter;
        for (char c : s) 
            counter[c]++;

        int res = 0, odds = 0;
        for (auto it = counter.begin(); it != counter.end(); it++) {
            odds += it->second % 2;
            res += it->second;
        }
        if (odds > 0)
            res -= odds - 1;
        
        return res;
    }
};