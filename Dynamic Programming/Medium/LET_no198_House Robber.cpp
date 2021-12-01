class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size(), prev = nums[0], prev2 = 0, res = 0;
        if (n <= 1)
            return nums[0];
        for (int i = 1; i < n; i++) {
            res = max(prev, prev2 + nums[i]);
            prev2 = prev;
            prev = res;
        }
        return res;
    }
};