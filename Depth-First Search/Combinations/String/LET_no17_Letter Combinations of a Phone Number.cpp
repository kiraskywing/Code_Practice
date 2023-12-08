class Solution {
public:
    vector<string> letterCombinations(string digits) {
        if (digits.size() == 0)
            return {};
        
        string memo[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        vector<string> res;
        string temp = "";
        helper(digits, 0, memo, temp, res);
        return res;
    }

    void helper(string& digits, int start, string memo[], string& temp, vector<string>& res) {
        if (start == digits.size()) {
            res.push_back(temp);
            return;
        }

        for (char c : memo[digits[start] - '0']) {
            temp.push_back(c);
            helper(digits, start + 1, memo, temp, res);
            temp.pop_back();
        }
    }
};