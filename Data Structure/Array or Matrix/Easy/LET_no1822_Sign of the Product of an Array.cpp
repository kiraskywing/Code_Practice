class Solution {
public:
    int arraySign(vector<int>& nums) {
        int res = 1;
        for (int num : nums) {
            if (num == 0)
                return 0;
            res *= (num < 0) ? -1 : 1;
        }

        return res;
    }
};