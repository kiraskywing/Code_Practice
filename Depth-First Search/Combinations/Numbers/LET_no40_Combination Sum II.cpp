class Solution {
private:
    int n;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        n = candidates.size();
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> temp;
        helper(candidates, 0, target, temp, res);
        return res;
    }

    void helper(vector<int>& candidates, int start, int target, vector<int>& temp, vector<vector<int>>& res) {
        if (target < 0)
            return;
        if (target == 0) {
            res.push_back(temp);
            return;
        }

        for (int i = start; i < n; i++) {
            if (i != start && candidates[i] == candidates[i - 1])
                continue;
            temp.push_back(candidates[i]);
            helper(candidates, i + 1, target - candidates[i], temp, res);
            temp.pop_back();
        }
    }
};