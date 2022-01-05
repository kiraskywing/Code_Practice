class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> temp;
        dfs(res, s, temp, 0);
        return res;
    }
    
    void dfs(vector<vector<string>>& res, string& s, vector<string>& temp, int start) {
        if (start == s.size()) {
            res.push_back(temp);
            return;
        }
        
        for (int i = start; i < s.size(); i++) {
            if (isPalindrome(s, start, i)) {
                temp.push_back(s.substr(start, i - start + 1));
                dfs(res, s, temp, i + 1);
                temp.pop_back();
            }
        }
    }
    
    bool isPalindrome(string& s, int left, int right) {
        while (left <= right) {
            if (s[left++] != s[right--])
                return false;
        }
        return true;
    }
};