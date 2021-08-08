class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> res;
        for (int i = 0; i <= n; i++)
            res.push_back(i - 1);
        
        vector<vector<bool>> isPalindrome = getPalindrome(s);
        
        for (int length = 1; length <= n; length++) {
            for (int i = 0; i < length; i++) {
                if (isPalindrome[i][length - 1])
                    res[length] = min(res[length], res[i] + 1);
            }
        }
        
        return res[n];
    }
    
    vector<vector<bool>> getPalindrome(string s) {
        int n = s.size();
        vector<vector<bool>> res(n, vector<bool>(n, false));
            
        for (int i = 0; i < n; i++) {
            res[i][i] = true;
            if (i < n - 1)
                res[i][i + 1] = s[i] == s[i + 1];
        }
        
        for (int d = 2; d < n; d++) {
            for (int i = 0; i < n - d; i++)
                res[i][i + d] = res[i + 1][i + d - 1] && s[i] == s[i + d];
        }
        
        return res;
    }
};