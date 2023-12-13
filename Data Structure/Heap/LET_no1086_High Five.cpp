class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        unordered_map<int, priority_queue<int, vector<int>, greater<int>>> memo;
        for (vector<int>& item : items) {
            memo[item[0]].push(item[1]);
            if (memo[item[0]].size() > 5)
                memo[item[0]].pop();
        }

        vector<vector<int>> res;
        for (auto& [key, vals] : memo) {
            int cur = 0;
            while (!vals.empty()) {
                cur += vals.top();
                vals.pop();
            }
            res.push_back({key, cur / 5});
        }

        sort(res.begin(), res.end(), [](vector<int>& a, vector<int>& b){ return a[0] < b[0]; });
        return res;
    }
};