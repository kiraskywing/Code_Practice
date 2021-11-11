class Solution {
public:
    int minStartValue(vector<int>& nums) {
        int res = 1, cur = 0;
        for (int i : nums) {
            cur += i;
            res = max(res, -cur + 1);
        }
        return res;
    }
};