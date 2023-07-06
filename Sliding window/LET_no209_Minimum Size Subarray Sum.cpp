class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, n = nums.size(), res = n + 1;
        for (int right = 0; right < n; right++) {
            target -= nums[right];
            while (left <= right && target <= 0) {
                res = min(res, right - left + 1);
                target += nums[left++];
            }
        }

        return (res == n + 1 ? 0 : res);
    }
};