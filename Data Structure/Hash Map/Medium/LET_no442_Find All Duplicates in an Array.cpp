class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        for (int i : nums) {
            if (nums[abs(i) - 1] < 0)
                res.push_back(abs(i));
            else
                nums[abs(i) - 1] *= -1;
        }
        return res;
    }
};