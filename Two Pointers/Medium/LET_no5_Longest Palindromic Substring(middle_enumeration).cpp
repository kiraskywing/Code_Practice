class Solution {
public:
    string longestPalindrome(string s) {
        int res_left = 0, res_right = 0;
        for (int i = 0; i < s.size(); i++) {
            pair<int, int> interval = GetSubstringInterval(s, i, i);
            if (interval.second - interval.first > res_right - res_left) {
                res_left = interval.first;
                res_right = interval.second;
            }

            if (i > 0) {
                pair<int, int> interval = GetSubstringInterval(s, i - 1, i);
                if (interval.second - interval.first > res_right - res_left) {
                    res_left = interval.first;
                    res_right = interval.second;
                }
            }
        }

        return s.substr(res_left, res_right - res_left + 1);
    }

    pair<int, int> GetSubstringInterval(string& s, int left, int right) {
        int n = s.size();
        while (left >= 0 && right < n && s[left] == s[right]) {
            left--;
            right++;
        }
        
        return {left + 1, right - 1};
    }
};