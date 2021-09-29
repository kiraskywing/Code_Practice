class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& nums) {
        for (int i = 0, j = 1; i < nums.size() && j < nums.size(); ) {
            if (nums[i] % 2 == 0) i += 2;
            else if (nums[j] % 2 == 1) j += 2;
            else swap(nums[i], nums[j]);
        }
        return nums;
    }
};