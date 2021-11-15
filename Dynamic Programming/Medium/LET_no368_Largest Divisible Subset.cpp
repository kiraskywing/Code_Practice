class Solution {
public:
    vector<int> largestDivisibleSubset(vector<int>& nums) {
        int n = nums.size();
        if (n <= 1)
            return nums;
        
        vector<int> dp(n, 1);
        sort(nums.begin(), nums.end());
        int count = INT_MIN;
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0)
                    dp[i] = max(dp[i], dp[j] + 1);
            }
            count = max(count, dp[i]);
        }
        
        vector<int> res;
        int prev = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (dp[i] == count && prev % nums[i] == 0) {
                res.push_back(nums[i]);
                count--;
                prev = nums[i];
            }
        }
        
        return res;
    }
};