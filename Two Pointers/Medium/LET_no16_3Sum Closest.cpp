class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int res = INT_MAX, n = nums.size();
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;

            int left = i + 1, right = n - 1;
            while (left < right) {
                int cur = nums[left] + nums[right] + nums[i];
                if (abs(long(target) - cur) < abs(long(target) - res))
                    res = cur;

                if (cur < target) {
                    left++;
                    while (left < right && nums[left] == nums[left - 1])
                        left++;
                }
                else {
                    right--;
                    while (left < right && nums[right] == nums[right + 1])
                        right--;
                }
            }
        }

        return res;
    }
};