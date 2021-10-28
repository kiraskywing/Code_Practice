class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        if (!n)
            return {};
        
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < n - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1])
                continue;
            
            int j = i + 1, k = n - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                if (total < 0)
                    j++;
                else if (total > 0)
                    k--;
                else {
                    res.push_back({nums[i], nums[j], nums[k]});
                    j++; k--;
                    while (j < k && nums[j] == nums[j - 1])
                        j++;
                    while (j < k && nums[k] == nums[k + 1])
                        k--;
                }
            }
        }
        return res;
    }
};