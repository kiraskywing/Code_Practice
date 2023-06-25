class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double min_val = *min_element(nums.begin(), nums.end()) * 1.0;
        double max_val = *max_element(nums.begin(), nums.end()) * 1.0;

        while (min_val + 1e-5 <= max_val) {
            double mid_val = min_val + (max_val - min_val) / 2;
            if (hasSubarray(nums, k, mid_val))
                min_val = mid_val;
            else
                max_val = mid_val;
        }

        if (hasSubarray(nums, k, max_val))
            return max_val;
        return min_val;
    }

    bool hasSubarray(vector<int>& nums, int k, double average) {
        double cur = 0.0, pre = 0.0, pre_min = 0.0;
        for (int i = 0; i < k - 1; i++)
            cur += nums[i] - average;
        
        for (int i = k - 1; i < nums.size(); i++) {
            cur += nums[i] - average;
            if (cur >= pre_min)
                return true;
            
            pre += nums[i - k + 1] - average;
            pre_min = min(pre_min, pre);
        }

        return false;
    }
};