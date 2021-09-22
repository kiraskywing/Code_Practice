class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int res = 0, cur = 0;
        for (int i : nums) {
            cur = i ? cur + 1 : 0;
            res = max(res, cur);
        }
        return res;
    }
};