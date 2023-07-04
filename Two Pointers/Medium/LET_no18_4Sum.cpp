class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        vector<vector<int>> res;

        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            for (int j = i + 1; j < n - 2; j++) {
                if (j > i + 1 && nums[j] == nums[j - 1])
                    continue;

                int left = j + 1, right = n - 1;
                long remain = long(target) - nums[i] - nums[j];

                while (left < right) {
                    int cur = nums[left] + nums[right];
                    if (cur < remain) {
                        left++;
                        while (left < right && nums[left] == nums[left - 1])
                            left++;
                    }
                    else if (cur > remain) {
                        right--;
                        while (left < right && nums[right] == nums[right + 1])
                            right--;
                    }
                    else {
                        res.push_back({nums[i], nums[j], nums[left], nums[right]});
                        left++;
                        while (left < right && nums[left] == nums[left - 1])
                            left++;
                        right--;
                        while (left < right && nums[right] == nums[right + 1])
                            right--;
                    }
                }
            }
        }

        return res;
    }
};