class Solution {
private:
    int n;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        n = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        vector<int> temp;
        helper(nums, 0, temp, res);
        return res;
    }

    void helper(vector<int>& nums, int start, vector<int>& temp, vector<vector<int>>& res) {
        res.push_back(temp);

        for (int i = start; i < n; i++) {
            temp.push_back(nums[i]);
            helper(nums, i + 1, temp, res);
            temp.pop_back();
        }
    }
};