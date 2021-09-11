class Solution {
public:
    int numberOfArithmeticSlices(vector<int>& nums) {
        int res = 0;
        unordered_map<long, int> dp[nums.size()];
        for (int i = 0; i < nums.size(); i++) {
            for (int j = 0; j < i; j++) {
                long diff = (long)nums[i] - nums[j];
                auto it = dp[j].find(diff);
                int count = it == dp[j].end() ? 0 : it->second;
                res += count;
                dp[i][diff] += count + 1;
            }
        }
        return res;
    }
};