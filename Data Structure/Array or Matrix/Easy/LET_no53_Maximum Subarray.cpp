class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int preSum = 0, preMin = 0, preMax = INT_MIN;
        for (int num : nums) {
            preSum += num;
            preMax = max(preMax, preSum - preMin);
            preMin = min(preMin, preSum);
        }
        return preMax;
    }
};