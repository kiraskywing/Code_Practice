class Solution {
private:
    int n;
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        n = nums.size();
        vector<vector<int>> res;
        vector<int> temp;
        sort(nums.begin(), nums.end());
        helper(nums, 0, temp, res);
        return res;
    }

    void helper(vector<int>& nums, int start, vector<int>& temp, vector<vector<int>>& res) {
        res.push_back(temp);

        for (int i = start; i < n; i++) {
            if (i != start && nums[i] == nums[i - 1])
                continue;

            temp.push_back(nums[i]);
            helper(nums, i + 1, temp, res);
            temp.pop_back();
        }
    }
};