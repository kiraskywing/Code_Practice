class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> memo;
        for (int num : nums)
            memo[num]++;

        int res = 0;
        for (auto it = memo.begin(); it != memo.end(); it++) {
            int cnt = it->second;
            if (cnt == 1)
                return -1;
            res += (cnt / 3);
            if (cnt % 3 != 0)
                res++;
        }

        return res;
    }
};