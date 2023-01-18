class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int cur_min = 0, cur_max = 0;
        int total_min = INT_MAX, total_max = INT_MIN, total_sum = 0;
        for (int num : nums) {
            cur_max = max(cur_max + num, num);
            total_max = max(total_max, cur_max);
            cur_min = min(cur_min + num, num);
            total_min = min(total_min, cur_min);
            total_sum += num;
        }

        return total_sum != total_min ? max(total_max, total_sum - total_min) : total_max;
    }
};