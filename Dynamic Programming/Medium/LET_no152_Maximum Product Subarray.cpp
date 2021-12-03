class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res, preMax, preMin, curMax, curMin;
        res = preMax = preMin = nums[0];
        for (int i = 1; i < nums.size(); i++) {
            curMax = max(nums[i], max(preMax * nums[i], preMin * nums[i]));
            curMin = min(nums[i], min(preMax * nums[i], preMin * nums[i]));
            res = max(res, curMax);
            preMax = curMax;
            preMin = curMin;
        }
        return res;
    }
};