class Solution {
public:
    int numSubseq(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), mod = 1e9 + 7;
        vector<int> power(n, 1);
        for (int i = 1; i < n; i++)
            power[i] = power[i - 1] * 2 % mod;
        
        int res = 0, left = 0, right = n - 1;
        while (left <= right) {
            if (nums[left] + nums[right] > target)
                right--;
            else {
                res = (res + power[right - left]) % mod;
                left++;
            }
        }

        return res;
    }
};