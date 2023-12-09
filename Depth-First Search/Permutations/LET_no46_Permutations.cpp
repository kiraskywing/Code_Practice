class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        queue<int> inputs;
        for (int num : nums)
            inputs.push(num);
        vector<vector<int>> res;
        vector<int> temp;
        helper(inputs, temp, res);
        return res;
    }

    void helper(queue<int>& inputs, vector<int>& temp, vector<vector<int>>& res) {
        if (inputs.empty()) {
            res.push_back(temp);
            return;
        }

        int n = inputs.size();
        while (n-- > 0) {
            int num = inputs.front();
            inputs.pop();
            temp.push_back(num);
            helper(inputs, temp, res);
            temp.pop_back();
            inputs.push(num);
        }
    }
};