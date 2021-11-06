class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        long diff = 0;
        for (int n : nums)
            diff ^= n;
        diff &= -diff;
        vector<int> res(2, 0);
        for (int n : nums)
            diff & n ? res[0] ^= n : res[1] ^= n;
        return res;
    }
};