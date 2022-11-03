class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        vector<vector<int>> memo(26, vector<int>(26, 0));
        int res = 0;
        for (string &w : words) {
            int a = w[0] - 'a';
            int b = w[1] - 'a';
            
            if (memo[b][a] > 0) {
                res += 4;
                memo[b][a]--;
            }
            else
                memo[a][b]++;
        }
        
        for (int i = 0; i < 26; i++) {
            if (memo[i][i] > 0) {
                res += 2;
                break;
            }
        }
        
        return res;
    }
};