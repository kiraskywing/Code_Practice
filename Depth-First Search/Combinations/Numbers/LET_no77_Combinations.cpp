class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        vector<int> temp;
        helper(n, k, 1, temp, res);
        return res;
    }

    void helper(int n, int k, int start, vector<int>& temp, vector<vector<int>>& res) {
        if (k == 0) {
            res.push_back(temp);
            return;
        }

        for (int i = start; i <= n; i++) {
            temp.push_back(i);
            helper(n, k - 1, i + 1, temp, res);
            temp.pop_back();
        }
    }
};