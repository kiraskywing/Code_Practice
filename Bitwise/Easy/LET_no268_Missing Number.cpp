class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int res = nums.size(), i = 0;
        for (int num : nums) {
            res ^= num;
            res ^= i++;
        }

        return res;
    }
};