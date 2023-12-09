class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        unordered_map<int, int> memo;
        for (int num : nums)
            memo[num] += 1;
        vector<vector<int>> res;
        vector<int> temp;
        helper(memo, nums.size(), temp, res);
        return res;
    }

    void helper(unordered_map<int, int>& memo, int n, vector<int>& temp, vector<vector<int>>& res) {
        if (temp.size() == n) {
            res.push_back(temp);
            return;
        }

        for (auto it = memo.begin(); it != memo.end(); it++) {
            if (it->second > 0) {
                it->second--;
                temp.push_back(it->first);
                helper(memo, n, temp, res);
                temp.pop_back();
                it->second++;
            }
        }
    }
};