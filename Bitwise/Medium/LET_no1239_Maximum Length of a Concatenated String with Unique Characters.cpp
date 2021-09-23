class Solution {
public:
    int maxLength(vector<string>& arr) {
        vector<bitset<26>> dp = {bitset<26>()};
        int res = 0;
        for (auto& s : arr) {
            bitset<26> a;
            for (char c : s)
                a.set(c - 'a');
            int n = a.count();
            if (n < s.size())
                continue;
            
            for (int i = dp.size() - 1; i >= 0; i--) {
                bitset b = dp[i];
                if ((a & b).any())
                    continue;
                dp.push_back(a | b);
                res = max(res, (int) b.count() + n);
            }
        }
        return res;
    }
};