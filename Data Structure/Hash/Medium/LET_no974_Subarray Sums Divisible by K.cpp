class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> memo(k, 0);
        memo[0] = 1;
        int prefix_sum = 0, res = 0;
        
        for (int num : nums) {
            prefix_sum = ((prefix_sum + num) % k + k) % k;
            res += memo[prefix_sum];
            memo[prefix_sum]++;
        }

        return res;
    }
};