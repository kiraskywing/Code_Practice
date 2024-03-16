class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int res = 0, cur = 0;
        unordered_map<int, int> memo;
        for (int i = 0; i < nums.size(); i++) {
            cur += nums[i] == 1 ? 1 : -1;
            if (cur == 0)
                res = max(res, i + 1);
            else {
                if (memo.count(cur))
                    res = max(res, i - memo[cur]);
                else
                    memo[cur] = i;
            }
        }

        return res;
    }
};