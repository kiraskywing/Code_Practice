class Solution {
public:
    int countSubstrings(string s) {
        int n = s.size();
        vector<vector<bool>> isPalindrome(n, vector<bool>(n, false));

        int res = 0;
        for (int d = 0; d < n; d++) {
            for (int left = 0; left < n - d; left++) {
                int right = left + d;
                isPalindrome[left][right] = s[left] == s[right] && (right - left < 3 || isPalindrome[left + 1][right - 1]);
                res += isPalindrome[left][right];
            }
        }

        return res;
    }
};