class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int cur = (1 << i), count = 0;

            for (int num : nums)
                count += int((cur & num) != 0);

            if (count % 3 != 0)
                res |= cur;
        }

        return res;
    }
};