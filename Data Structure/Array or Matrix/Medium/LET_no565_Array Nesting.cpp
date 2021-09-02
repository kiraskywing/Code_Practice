class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < nums.size(); i++) {
            int cur = 0;
            for (int j = i; nums[j] >= 0; cur++) {
                int temp = nums[j];
                nums[j] = -1;
                j = temp;
            }
            res = max(res, cur);
        }
        return res;
    }
};