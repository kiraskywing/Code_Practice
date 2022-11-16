class Solution {
public:
    int twoSumLessThanK(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int res = INT_MIN;
        int left = 0, right = nums.size() - 1;
        
        while (left < right) {
            int cur = nums[left] + nums[right];
            if (cur < k) {
                res = max(res, cur);
                left++;
            }
            else
                right--;
        }
        
        return res > INT_MIN ? res : -1;
    }
};