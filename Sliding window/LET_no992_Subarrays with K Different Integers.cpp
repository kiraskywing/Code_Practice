class Solution {
public:
    int subarraysWithKDistinct(vector<int>& nums, int k) {
        return helper(nums, k) - helper(nums, k - 1);
    }

    int helper(vector<int>& nums, int k) {
        unordered_map<int, int> memo;
        int left = 0, res = 0;
        for (int right = 0; right < nums.size(); right++) {
            int num = nums[right];
            k -= !memo[num];
            memo[num]++;
            while (k < 0) {
                memo[nums[left]]--;
                k += memo[nums[left]] == 0;
                left++;
            }

            res += right - left + 1;
        }

        return res;
    }
};