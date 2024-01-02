class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int, int> memo;
        int count = -1;
        for (int num : nums) {
            memo[num]++;
            count = max(count, memo[num]);
        }

        vector<vector<int>> res(count, vector<int>());
        for (auto it = memo.begin(); it != memo.end(); it++) {
            int num = it->first;
            count = it->second;
            for (int i = 0; i < count; i++)
                res[i].push_back(num);
        }

        return res;
    }
};